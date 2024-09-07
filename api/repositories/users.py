from ..data.db_config import get_connection

def getUserById(user_id: int):
    connection = get_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}
    
    else:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
        user = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        return user

def createNewUser(userName: str):
    connection = get_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}
    
    else:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (userName) VALUES (%s) RETURNING id;", (userName,))
        new_id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
        connection.close()
        
        return new_id

def getAllUsersDb():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users

    