import json
from ..data.db_config import get_connection
from ..models.logs import Log

def createLog(data: str):
     connection = get_connection()
     cursor= connection.cursor()
     cursor.execute("INSERT INTO logs (data) VALUES (%s)", (data,))
     connection.commit()
     cursor.close()
     connection.close()

def getAllLogs():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    cursor.close()
    connection.close()
    logs_list = [
        {
            'id': item[0],
            'data': item[1],
        }
        for item in logs
    ]
    json_result = json.dumps(logs_list)
    
    return json_result