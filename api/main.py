from fastapi import FastAPI, status
from api.routers.support import support
from api.routers.user import user
from api.routers.events import events

app = FastAPI()

app.include_router(support.supportRouter)
app.include_router(user.userRouter)
app.include_router(events.eventsRouter)


@app.get("/")
def api():
    return {"message": "Hello Api Finkargo"}