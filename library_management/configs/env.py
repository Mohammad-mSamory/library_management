from os import getenv

DB_HOST = getenv('DB_HOST', 'localhost')
DB_NAME = getenv('DB_NAME', 'library_management')
DB_PASSWORD = getenv('DB_PASSWORD', 'mohapass')
DB_PORT = getenv('DB_PORT', '5432')
DB_USER = getenv('DB_USER', 'mohasam2')
