import json
from ..data.db_config import get_connection
from ..models.support_model import Support

def getSupportByIdRepositorie(support_id: int):
    connection = get_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}
    
    else:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM support_cases WHERE id = %s;", (support_id,))
        support = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        return support

def createNewSupport(support: Support):
    connection = get_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}
    
    else:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO support_cases (case_name, description, created_at, user_id) VALUES (%s, %s, %s, %s) RETURNING id;", (support.case_name, support.description, support.created_at, support.user_id,))
        new_id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
        connection.close()
        
        return new_id

def getAllSupportDb():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
            SELECT s.*, u.username 
            FROM support_cases s 
            INNER JOIN users u ON s.user_id = u.id;
        """)
    support = cursor.fetchall()
    cursor.close()
    connection.close()
    print(support)
    support_list = [
        {
            'id': item[0],
            'case_name': item[1],
            'description': item[2],
            'created_at': item[3].isoformat(),
            'user_id': item[4],
            'username': item[5]
        }
        for item in support
    ]
    json_result = json.dumps(support_list)
    
    return json_result

def deleteSupport(support_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM support_cases WHERE id = %s;", (support_id,))
    cursor.execute("SELECT * FROM support_cases")
    support = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    support_list = [
    {
        'id': item[0],
        'case_name': item[1],
        'description': item[2],
        'created_at': item[3].isoformat(),
        'user_id': item[4]
    }
    for item in support
    ]
    json_result = json.dumps(support_list)
    
    return json_result