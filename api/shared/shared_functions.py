def converToObjects(list: list):
    return [{"id": item[0], "userName": item[1]} for item in list]
