read -p 'Mot de passe root:' MYSQL_PASS

sudo /etc/init.d/mariadb stop
sudo mysqld_safe --skip-grant-tables &
mysql -u root -p$MYSQL_PASS -e "GRANT ALL ON *.* TO 'dux'@'localhost' IDENTIFIED BY '$MYSQL_PASS' WITH GRANT OPTION;"
mysql -u root -p$MYSQL_PASS -e "use mysql;"
mysql -u root -p$MYSQL_PASS -e "flush privileges;"
quit
sudo /etc/init.d/mariadb stop
sudo /etc/init.d/mariadb start
