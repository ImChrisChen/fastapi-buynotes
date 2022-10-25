import uvicorn
from api import app  # 这里的 app 要和 main:app对应
from fastapi.staticfiles import StaticFiles
from fastapi import Request, Response

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


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
