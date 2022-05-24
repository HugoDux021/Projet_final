## Installation de python et de bibliothèques nécessaires

apt-get update
apt install -y python3 python3-pip


## Récupération de l'archive
#wget 'https://docs.google.com/uc?export=download&id=1v-6MUPYpwEiiwxMAukpC4CPfMoGKeY54' -O tp-sql.tar.gz 

## Décompression de l'archive
#tar -xzf tp-sql.tar.gz

## Intaller mariadb et le connecteur pour Python

apt install -y mariadb-server libmariadb3 libmariadb-dev
pip3 install mariadb

## Configurer mariadb

### Soit en lançant le script

apt install -y expect

read -p 'Mot de passe root:' MYSQL_PASS

MYSQL_ROOT_PASSWORD=""

SECURE_MYSQL=$(expect -c "
 set timeout 10
  spawn mysql_secure_installation
  expect "Enter current password for root \(enter for none\):"
  send -- "$MYSQL_ROOT_PASSWORD\r"
  expect "Set root password?"
  send -- "y\r"
  expect "New password:"
  send -- "${MYSQL_PASS}\r"
  expect "Re-enter new password:"
  send -- "${MYSQL_PASS}\r"
  expect "Remove anonymous users?"
  send -- "y\r"
  expect "Disallow root login remotely?"
  send -- "y\r"
  expect "Remove test database and access to it?"
  send -- "y\r"
  expect "Reload privilege tables now?"
  send -- "y\r"
  expect eof
")

echo "$SECURE_MYSQL"

## Créer l'utilisateur de base de données
read -p 'Nom utilisateur DB: ' USER_DB
read -p 'Mot de passe utilisateur DB: ' USER_DB_PASSWORD

mysql -u root -p$MYSQL_PASS -e "GRANT ALL ON *.* TO '$USER_DB'@'localhost' IDENTIFIED BY '$USER_DB_PASSWORD' WITH GRANT OPTION;"

mysql -u root -p$MYSQL_PASS -e "FLUSH PRIVILEGES;"

## Mettre à jour les informations dans le fichier config.py

sed -i "s/'user' : 'admin'/'user' : '$USER_DB'/" ./tp-sql/app-python/config.py
sed -i "s/'password' : 'password'/'password' : '$USER_DB_PASSWORD'/" ./tp-sql/app-python/config.py

## Créer la base et sa structure

mysql -u $USER_DB -p$USER_DB_PASSWORD < ./tp-sql/create_structure.sql

## Créer un utilisateur système et lui donner les droits d'éxecuter Python
read -p 'Nom utilisateur systeme: ' USER
read -p 'Mot de passe utilisateur système: ' USER_PASSWORD

egrep "^$USER" /etc/passwd >/dev/null
	if [ $? -eq 0 ]; then
		echo "$USER existe!"
		exit 1
	else
		pass=$(perl -e 'print crypt($ARGV[0], "password")' $USER_PASSWORD)
		useradd -m -p "$USER_PASSWORD" "$USER"
		[ $? -eq 0 ] && echo "L'utilisateur a été ajouté au système!" || echo "Echec de l'ajout de l'utilisateur!"
	fi

## Créer un groupe, ajouter l'utilisateur au groupe et définir le groupe comme propriétaire du binaire de python

groupadd python_app
usermod -a -G python_app $USER
chgrp python_app /usr/bin/python3 

## Se connecter avec l'utilisateur système et  Lancer l'application

su $USER -c 'python3 tp-sql/app-python/main.py'
