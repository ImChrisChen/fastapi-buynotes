import uvicorn
from api import app  # 这里的 app 要和 main:app对应
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
