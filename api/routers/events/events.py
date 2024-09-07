from fastapi import APIRouter, status

from api.helpers.events import deleteEventByIdHelper, getEventByIdHelper, createEventHelper, getAllEventsHelper, deleteEventByIdHelper

from ...models.events_model import Event

eventsRouter = APIRouter()

@eventsRouter.get("/events/{event_id}", status_code=status.HTTP_200_OK)
def getEventById(event_id: int):
    return getEventByIdHelper(event_id)

@eventsRouter.get("/events/", status_code=status.HTTP_200_OK)
def getAllEvents():
    return getAllEventsHelper()

@eventsRouter.post("/events/", status_code=status.HTTP_201_CREATED)
def createEvent(event: Event):
    return createEventHelper(event)

@eventsRouter.delete("/events/{event_id}", status_code=status.HTTP_200_OK)
def deleteEvent(event_id: int):
    return deleteEventByIdHelper(event_id)
