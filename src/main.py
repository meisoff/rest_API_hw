from fastapi import FastAPI
import crud

tags_metadata = [
    {
        "name": "Users",
        "description": "Операции с пользователями",
    },
    {
        "name": "Fuels",
        "description": "Операции с топливом",
    },

]

app = FastAPI(openapi_tags=tags_metadata)


@app.get("/get_filling", tags=["Fuels"])
def get_fill(id: int):
    return crud.get_fill(id)


@app.get("/fuels", tags=["Fuels"])
def get_fuel(id: int):
    return crud.get_fuel(id)


@app.post("/add_fuels", tags=["Fuels"])
def add_fuels(name: str, descr: str, price: float):
    obj = {
        "name": name,
        "description": descr,
        "price": price
    }

    return crud.add_fuels(obj)

@app.get("/get_users", tags=["Users"])
def get_users():
    return crud.get_all_client()


@app.post("/update_user", tags=["Users"])
def update_info(id: int, fio: str = None, phone: str = None, address: str = None, email: str = None, card: int = None):
    obj = {
        "fio": fio,
        "phone": phone,
        "address": address,
        "email": email,
        "card": card
    }
    return crud.update_client_info(id, obj)


@app.delete("/delete_user", tags=["Users"])
def delete_user(id: int):
    return crud.delete_client(id)
