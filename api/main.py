from fastapi import FastAPI, status
from api.routers.support import support
from api.routers.user import user
from api.routers.events import events
from api.routers.logs import logs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(support.supportRouter)
app.include_router(user.userRouter)
app.include_router(events.eventsRouter)
app.include_router(logs.logsRouter)


@app.get("/")
def api():
    return {"message": "Hello Api Finkargo"}