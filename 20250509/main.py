from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello() :
    return {"message": "Hello FastAPI"}

@app.get("/use")
async def nihao():
    return {"message": "nihao"}

@app.get("/problems")
async def problems():
    return {
        "문제들" : {
            "고": {"고장", "장고", "고윤", "고 언어", "고라니"},
            "장" : {"고장", "장고", "장한울"}

        }        
    }

@app.get("/user/{user}/{name}/{age}")
async def userInfo(user: str, name: str, age: int):
    return {
        "user" : user,
        "nickname" : name,
        "age" : age
    }

@app.get("/items")
async def item_name(q: str = None):
    if q:
        return {
            "items" : q
        }
    return {
        "items" : "NO"
    }
