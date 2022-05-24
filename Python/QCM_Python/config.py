import os
config = {
    'user' : os.getenv('USER_DB'),
    'password' : os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': '3306',
    'database': 'Registre_QCM',
}