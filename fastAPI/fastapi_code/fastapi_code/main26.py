# 中间件的使用2
from fastapi import FastAPI

app = FastAPI()


@app.middleware('http')
async def middleware1(request, call_next):
    print('中间件1:请求前')
    response = await call_next(request)
    print('中间件1:请求后')
    return response


@app.middleware('http')
async def middleware2(request, call_next):
    print('中间件2:请求前')
    response = await call_next(request)
    print('中间件2:请求后')
    return response

# 创建一个中间件记录日志信息


class LogMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        print('中间件3:请求前')
        await self.app(scope, receive, send)
        print('中间件3:请求后')


app.add_middleware(LogMiddleware)


@app.get('/middle')
async def get_middle():
    print('逻辑处理完成！')
    return '这是中间件'


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main26:app', host="127.0.0.1", port=8000, reload=True)
