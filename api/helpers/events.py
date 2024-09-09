from ..models.events_model import Event
from fastapi import HTTPException, status
from .logs import createNewLog

from api.repositories.events import getAllEventsDb, getEventByIdRepositorie, createNewEvent, deleteEvent

def getEventByIdHelper(event_id: int):
    eventFound = getEventByIdRepositorie(event_id)
    try:
        if eventFound is None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event Id not found")
        
        return {"event": eventFound, "status": status.HTTP_200_OK}

    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        createNewLog(f"Error executing the getEventById query - {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query get event {event_id}")
    
def createEventHelper(event: Event):
    event_id = createNewEvent(event)
    try:
        return {"id": event_id, "status": status.HTTP_200_OK}

    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        createNewLog(f"Error executing the create event query - {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query new event")

def getAllEventsHelper():
    try:
        events_list = getAllEventsDb()
        return {"events": events_list, "status": status.HTTP_200_OK}
    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        createNewLog(f"Error executing the getAll events query - {e}")
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error getting all events ")

def deleteEventByIdHelper(event_id: int):
    try:
        result = deleteEvent(event_id)
        return {"status": status.HTTP_200_OK, "events": result}
    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        createNewLog(f"Error executing the delete event query - {e}")
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error delete event bby id ")