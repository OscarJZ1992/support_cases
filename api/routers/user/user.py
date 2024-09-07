from fastapi import APIRouter, status

from ...models.user_model import User
from ...helpers.users import getAllUsersHelper, getUserHelper, createUserHelper
userRouter = APIRouter()

@userRouter.get("/user/{user_id}", status_code=status.HTTP_200_OK)
def getUser(user_id: int):
    return getUserHelper(user_id)

@userRouter.get("/users/", status_code=status.HTTP_200_OK)
def getAllUsers():
    return getAllUsersHelper()

@userRouter.post("/user/", status_code=status.HTTP_201_CREATED)
def createUser(user: User):
    return createUserHelper(user)
    
