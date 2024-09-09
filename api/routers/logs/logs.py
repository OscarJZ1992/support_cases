from fastapi import APIRouter, status

from api.helpers.logs import getAll

from ...models.support_model import Support

logsRouter = APIRouter()

@logsRouter.get("/logs/", status_code=status.HTTP_200_OK)
def getSupportById():
    return getAll()