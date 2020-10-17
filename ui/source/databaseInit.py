import psycopg2
from config.settings import DATABASES

connection = psycopg2.connect(user=DATABASES['default']['USER'],
                              password=DATABASES['default']['PASSWORD'],
                              host=DATABASES['default']['HOST'],
                              port=DATABASES['default']['PORT'],
                              )
#                              database="postgres_db")
connection.autocommit = True
cursor = connection.cursor()

cursor.execute("SELECT 1 FROM pg_database WHERE datname = '"+DATABASES['default']['NAME']+"'")
record = cursor.fetchone()
if record == None:        
    cursor.execute("CREATE DATABASE "+DATABASES['default']['NAME'])
    print("Created database " + DATABASES['default']['NAME'])
else:
    print("Database " + DATABASES['default']['NAME'] + " already exists.")
