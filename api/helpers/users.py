from fastapi import HTTPException, status

from api.models.user_model import User
from api.shared.shared_functions import converToObjects
from ..repositories.users import getUserById, createNewUser, getAllUsersDb, getUserByName, deleteUserById


def getUserHelper(user_id: int):
    userFound = getUserById(user_id)
    try:
        if userFound is None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Id not found")
        
        return {"user": userFound}

    except Exception as e:
        print(f"Error generated executing the query getUshelper: {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query get user {user_id}")

def getUserNameHelper(user_name: str):
    userFound = getUserByName(user_name)
    try:
        if userFound is None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Name not found")
        
        return {"id": userFound[0], "userName": userFound[1], "status": status.HTTP_200_OK}

    except Exception as e:
        print(f"Error generated executing the query geUserName: {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query get user {user_name}")
    
def createUserHelper(user: User):
    new_user = createNewUser(user.userName)
    try:
        return {"id": new_user, "userName": user.userName, "status": status.HTTP_200_OK}

    except Exception as e:
        print(f"Error generated executing the CreateUseHelper: {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query new user")

def getAllUsersHelper():
    try:
        users_list = getAllUsersDb()
        user_list_object = converToObjects(users_list)
        return {"users": user_list_object, "status": status.HTTP_200_OK}
    except Exception as e:
        print(f"Error generated executing the query getAllUser: {e}")
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error getting all users ")
    
def deleteUserHelper(user_id: int):
    try:
        userFound = deleteUserById(user_id)
        if userFound is None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Id not found")
        
        return {"id": user_id, "status": status.HTTP_200_OK}
    except Exception as e:
        print(f"Error generated executing the query delete {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query delete user {user_id}")