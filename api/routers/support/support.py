from fastapi import APIRouter, status

from api.helpers.support import getSupportByIdHelper, createSupportHelper, getAllSupportHelper, deleteSupportByIdHelper

from ...models.support_model import Support

supportRouter = APIRouter()

@supportRouter.get("/support/{support_id}", status_code=status.HTTP_200_OK)
def getSupportById(support_id: int):
    return getSupportByIdHelper(support_id)

@supportRouter.get("/support/", status_code=status.HTTP_200_OK)
def getAllSupport():
    return getAllSupportHelper()

@supportRouter.post("/support/", status_code=status.HTTP_201_CREATED)
def createSupport(support: Support):
    return createSupportHelper(support)

@supportRouter.delete("/support/{support_id}", status_code=status.HTTP_200_OK)
def deleteSupport(support_id: int):
    return deleteSupportByIdHelper(support_id)
