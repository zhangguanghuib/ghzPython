# 中间件的使用
from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.middleware('http')
async def middleware1(request, call_next):
    print('处理业务：之前')
    print(request.method, request.url)
    # if request.url.path == '/middle':
    # print('这个用户访问了middle接口')
    # return Response(content="你没有权限访问该接口")
    response = await call_next(request)
    response.headers['X-Token'] = '123456'
    print('处理业务：之后')
    return response


@app.get('/middle')
async def get_middle():
    print('处理业务：处理中')
    return '业务逻辑处理结果'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main25:app', host="127.0.0.1", port=8000, reload=True)
