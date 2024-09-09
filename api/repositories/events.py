import json
from ..data.db_config import get_connection
from ..models.events_model import Event

def getEventByIdRepositorie(event_id: int):
    connection = get_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}
    
    else:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM events WHERE id = %s;", (event_id,))
        event = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        return event

def createNewEvent(event: Event):
    connection = get_connection()
    if connection is None:
        return {"error": "No se pudo conectar a la base de datos"}
    else:
        print(event)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO events (action_type, created_at, user_id, information) VALUES (%s, %s, %s, %s) RETURNING id;", (event.action_type, event.created_at, event.user_id, event.information))
        new_id = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
        connection.close()
        return new_id

def getAllEventsDb():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
            SELECT e.*, u.username 
            FROM events e 
            INNER JOIN users u ON e.user_id = u.id;
        """)
    events = cursor.fetchall()
    cursor.close()
    connection.close()
    events_list = [
        {
            'id': item[0],
            'action_type': item[1],
            'user_id': item[3],
            'created_at': item[2].isoformat(),
            'information': item[4],
            'username': item[5]
        }
        for item in events
    ]
    json_result = json.dumps(events_list)
    
    return json_result

def deleteEvent(event_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM events WHERE id = %s;", (event_id,))
    connection.commit()
    cursor.execute("SELECT * FROM events")
    events = cursor.fetchall()
    cursor.close()
    connection.close()
    events_list = [
        {
            'id': item[0],
            'action_type': item[1],
            'user_id': item[3],
            'created_at': item[2].isoformat(),
            'information': item[4]
        }
        for item in events
    ]
    json_result = json.dumps(events_list)
    
    return json_result