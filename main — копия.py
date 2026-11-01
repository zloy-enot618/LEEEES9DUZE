from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()


animals = [
    {
        "id": 1,
        "name": "Лев",
        "value": 9,
        "risk": "Экстремальный"
    },
    {
        "id": 2,
        "name": "Орёл",
        "value": 17,
        "risk": "Средний"
    },
    {
        "id": 3,
        "name": "Утка",
        "value": 189,
        "risk": "Минимальный"
    },
    {
        "id": 4,
        "name": "Горилла",
        "value": 3,
        "risk": "ОЧЕНЬ ЭКСТРЕМАЛЬНЫЙ"
    },
    {
        "id": 5,
        "name": "Слоник",
        "value": 3,
        "risk": "Минимальный"
    }
]

class Animals(BaseModel):
    id: int
    name: str
    value: int
    risk: str


class AddAnimal(BaseModel):
    name: str
    value: int
    risk: str


@app.get("/", response_class=HTMLResponse)
def say_hello():
    html_hello = """
    <!DOCTYPE html>

    <html>
        <head>
            <title>Hello!</title>
        </head>
        <body>
            <h1>Привет! \nЗайди на /docs.</h1>
        </body>

    </html>
"""
    return HTMLResponse(content=html_hello)



@app.get("/animals", response_model=list[Animals])
def get_animals():
    return animals


@app.post("/animals", response_model=Animals, status_code=201)
def add_animal(animal: AddAnimal):
    am_id = len(animals) + 1

    new_animal = {
        "id": am_id,
        "name": animal.name,
        "value": animal.value,
        "risk": animal.risk
    }
    animals.append(new_animal)
    return new_animal
    

@app.put("/animals/{animal_id}", response_model=Animals) #просто изменение записи в датабазе, никакой операции на животных! xd lol :D
def uptade_animal(animal_id: int, animal: AddAnimal): #its просто learning! онли code, обучение delete,post и тд, PETA - не бей пж :)
    for saved_animal in animals:
        if saved_animal["id"] == animal_id:
            saved_animal["id"] = animal_id #никакого вскрытия!! xd lol :() -> просто меняем айди, имя, и кол-во животных, а так же риск
            saved_animal["name"] = animal.name #peta, если животных стало меньше, они просто сбежали и находятся в гуд условиях.
            saved_animal["value"] = animal.value
            saved_animal["risk"] = animal.risk
            return saved_animal
    raise HTTPException(
        status_code=404,
        detail="Животное не найдено!" #not in zoo or escaped, not killed! its not reallife xd pls lol! only learning.
    )

@app.delete("/animals/{animal_id}", response_model=list[Animals])
def delete_animal(animal_id: int): #from database, not reallife xd lol. :D, it's test project, im learning post,get,put,delete only .!! 
    for index, saved_animal in enumerate(animals):
        if saved_animal["id"] == animal_id:
            deleted_animal = animals.pop(index) #from database lol! no f**** animal killing! it's just db detele func, it's not real :D.
            return deleted_animal #просто отпускаем их ок?

