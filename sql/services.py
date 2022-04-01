from django.db import connection
from decouple import config

def my_custom_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()

    return row


def create_user(username):
    with connection.cursor() as cursor:
        cursor.execute(
            f'''
                CREATE USER student WITH PASSWORD 'test';
                GRANT CONNECT ON DATABASE {config('NAME')} TO student;
                GRANT USAGE ON SCHEMA itschool_sql TO student;
                GRANT SELECT ON sql_product TO student;
                GRANT SELECT ON sql_customer TO student;
                GRANT SELECT ON sql_company TO student;
            '''
        )
