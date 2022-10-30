import uvicorn  # 这里的 app 要和 main:app对应
from fastapi.staticfiles import StaticFiles
from fastapi import Request, Response, FastAPI
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware
from src import api

app = FastAPI()

app.include_router(api.router)

app.add_middleware(
    CORSMiddleware,  # https://fastapi.tiangolo.com/zh/tutorial/cors/
    allow_origins=["*.tpddns.cn"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

ResponseCodeMsg = dict(
    success=(0, "ok"),
    error=(-1, 'error'),
)


def http_response_wrapper(code: int, data=None, msg: str = 'ok'):
    if data is None:
        data = {}
    return {
        'code': code,
        'data': data,
        'msg': msg,
    }


@app.middleware('http')
async def add_http_middleware(request: Request, call_next):
    response: Response = await call_next(request)
    return response
    # if response.status_code == 200:
    #     code, msg = ResponseCodeMsg['success']
    #     response = http_response_wrapper(code=code, data={}, msg=msg)
    # return response


@app.get('/')
async def fastapi_buynotes():
    content = '<h1>Hello FastAPI</h1>'
    return HTMLResponse(content=content, status_code=200)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True,host='0.0.0.0')
