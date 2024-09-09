from fastapi import status 
from ..repositories.logs import createLog, getAllLogs

def createNewLog(data: str):
    try:
        createLog(data)
    except Exception as e:
        print(e)
        return False
    
def getAll():
    try:
        logs = getAllLogs()
        return {"status": status.HTTP_200_OK, "logs": logs}
    except Exception as e:
        print(e)
        return False