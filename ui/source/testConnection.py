import psycopg2
from config.settings import DATABASES

connection = psycopg2.connect(user=DATABASES['default']['USER'],
                              password=DATABASES['default']['PASSWORD'],
                              host=DATABASES['default']['HOST'],
                              port=DATABASES['default']['PORT'],
                              )
cursor = connection.cursor()
cursor.execute("SELECT 1")
print("Connected!")
