from fastapi import APIRouter, status

from ...models.user_model import User
from ...helpers.users import getAllUsersHelper, getUserNameHelper, getUserHelper, createUserHelper, deleteUserHelper
userRouter = APIRouter()

@userRouter.get("/user/{user_id}", status_code=status.HTTP_200_OK)
def getUser(user_id: int):
    return getUserHelper(user_id)

@userRouter.get("/user/", status_code=status.HTTP_200_OK)
def getUserName(user_name: str):
    return getUserNameHelper(user_name)

@userRouter.get("/users/", status_code=status.HTTP_200_OK)
def getAllUsers():
    return getAllUsersHelper()

@userRouter.post("/user/", status_code=status.HTTP_201_CREATED)
def createUser(user: User):
    return createUserHelper(user)

@userRouter.delete("/user/{user_id}", status_code=status.HTTP_200_OK)
def deleteUser(user_id: int):
    return deleteUserHelper(user_id)