import uvicorn  # 这里的 app 要和 main:app对应
from fastapi.staticfiles import StaticFiles
from fastapi import Request, Response, FastAPI, Depends, Body, Header
from fastapi.responses import HTMLResponse

from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src import api
from src.interceptors.exception import UnicornException
from src.schemas.basic import ApiResponseModel, ApiCodeEnum


async def check_jwt_token(host=Header(...)):
    print(host)
    return host


app = FastAPI(
    title="fastapi-buynotes",
    version='0.0.1',
    # dependencies=[Depends(check_jwt_token)]
)


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        code=-1,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


app.include_router(api.router)

app.add_middleware(
    CORSMiddleware,  # https://fastapi.tiangolo.com/zh/tutorial/cors/
    allow_origins=["*.tpddns.cn"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.middleware('http')
async def add_http_middleware(request: Request, call_next):
    response: Response = await call_next(request)
    return response


@app.get('/')
async def fastapi_buynotes():
    return ApiResponseModel(ApiCodeEnum.OK)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host='0.0.0.0')
