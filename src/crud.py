import database

db = database.db


def get_fill(id: int):
    get_info = None

    for item in db["fill"]:
        if item["id"] == id:
            get_info = item

    if get_info:
        for item in db["fuel"]:
            if get_info["fuel"] == item["id"]:
                get_info["fuel"] = item

        for item in db["employee"]:
            if get_info["employee"] == item["id"]:
                get_info["employee"] = item

        for item in db["auto"]:
            if get_info["brand"] == item["id"]:
                get_info["brand"] = item

        for item in db["clients"]:
            if get_info["client"] == item["id"]:
                get_info["client"] = item

        return {"fuel": get_info, "err": 0, "total": len(db["fill"])}
    else:
        return {"err": 1, "description": "No such indexes"}


def get_fuel(id: int):
    item = None
    for i in db["fuel"]:
        if i["id"] == id:
            item = i

    if item:
        return {"fuel": item, "err": 0, "total": len(db["fuel"])}
    else:
        return {"err": 1, "description": "No such indexes"}


def add_fuels(obj: dict):
    count = len(db["fuel"])
    database.db["fuel"].append(
        {
            "id": count + 1,
            **obj
        }
    )
    return {"err": 0}


def get_all_client():
    clients = database.db["clients"]

    for i in clients:
        for j in database.db["cards"]:
            if i["card"] == j["id"]:
                i["card"] = j

    return {"clients": clients, "total": len(database.db["clients"])}


def update_client_info(id: int, obj: dict):
    client = None

    for i in db["clients"]:
        if id == i["id"]:
            client = i

    if client:
        for index, item in obj.items():
            if item:
                database.db["clients"][id - 1][index] = obj[index]
        return {"err": 0}
    else:
        return {"err": 1, "description": "No such indexes"}


def delete_client(id: int):
    if database.db["clients"][id - 1]:
        del database.db["clients"][id - 1]
        return {"err": 0}
    else:
        return {"err": 1, "description": "No such indexes"}
