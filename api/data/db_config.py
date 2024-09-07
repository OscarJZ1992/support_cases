import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            user='postgres',
            password='1234',
            host='localhost',
            port='5432',
            database='support_process_cases'
        )
        return connection
    except psycopg2.Error as error:
        print(f"Error connecting to database: {error}")
        return None