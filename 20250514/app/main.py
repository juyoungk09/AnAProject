from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def Path_Query() :
    return "helloworld"

@app.get("/items/{item}")
async def Path_Query(
    item: int = Path(..., ge=1, le=1000),
    q: str = Query(default=None, min_length=3, max_length=10, regex="^[a-zA-Z0-9?!_]*$")
    ):
    return {"item" : f"{item} {q}"}
class ItemModel(BaseModel) :
    name : str = Field(..., min_length=3, max_length=100)
    description : str
    price : float = Field(default=None, ge=1000, le=100000)
    tax : float = None
    imgs : list[str]

class ItemStar(BaseModel) :
    star: int
    comment : str

@app.post("/shop")
async def Item_shop(item : ItemModel, star: ItemStar):
    return item

class Project(BaseModel) :
    projectname : str = Field(..., min_length=3, max_length=20)
    owener : str
    description : str
    contributor : list[str]
    save : int
    good : int

@app.post("/project")
async def Project_Item(project : Project) :
    return project
