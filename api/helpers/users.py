from fastapi import HTTPException, status

from api.models.user_model import User
from api.shared.shared_functions import converToObjects
from ..repositories.users import getUserById, createNewUser, getAllUsersDb


def getUserHelper(user_id: int):
    userFound = getUserById(user_id)
    try:
        if userFound is None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Id not found")
        
        return {"user": userFound}

    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query get user {user_id}")
    
    
def createUserHelper(user: User):
    new_user = createNewUser(user.userName)
    try:
        return {"id": new_user, "userName": user.userName}

    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query new user")

def getAllUsersHelper():
    try:
        users_list = getAllUsersDb()
        user_list_object = converToObjects(users_list)
        return user_list_object
    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error getting all users ")