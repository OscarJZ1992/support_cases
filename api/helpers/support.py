from .logs import createNewLog
from ..models.support_model import Support
from fastapi import HTTPException, status

from api.repositories.support import getAllSupportDb, getSupportByIdRepositorie, createNewSupport, deleteSupport

def getSupportByIdHelper(support_id: int):
    supportFound = getSupportByIdRepositorie(support_id)
    try:
        if supportFound is None:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Support Id not found")
        
        return {"support": supportFound, "status": status.HTTP_200_OK}

    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        createNewLog(f"Error executing the get support by id query: {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query get support {support_id}")
    
def createSupportHelper(support: Support):
    support_id = createNewSupport(support)
    try:
        return {"id": support_id, "status": status.HTTP_200_OK}

    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        createNewLog(f"Error executing the create support query: {e}")
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error execute the query new support")

def getAllSupportHelper():
    try:
        support_list = getAllSupportDb()
        return {"supports": support_list, "status": status.HTTP_200_OK}
    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        createNewLog(f"Error executing the getAllSupport query: {e}")
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error getting all supports ")

def deleteSupportByIdHelper(support_id: int):
    try:
        result = deleteSupport(support_id)
        return {"status": status.HTTP_200_OK, "message": "Item deleted", "supports": result}
    except Exception as e:
        print(f"Error ejecutando la consulta: {e}")
        createNewLog(f"Error executing the delete support query: {e}")
        HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error delete support by id ")