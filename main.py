from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def test1():
    return "hello fastapi"


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000,reload=True)