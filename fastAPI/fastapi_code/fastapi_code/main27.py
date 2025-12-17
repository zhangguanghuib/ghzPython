# CORS使用
from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],   # 允许的域名 ：如  ['http://127.0.0.1:8080']
    allow_credentials=True,  # 允许携带cookie
    allow_methods=['*'],    # 允许的请求方法
    allow_headers=['*'],  # 允许的请求头
)

# @app.middleware('http')
# async def add_cors_headers(request, call_next):
#     # 处理option 请求
#     if request.method == 'OPTIONS':
#         headers = {
#             "Access-Control-Allow-Origin": '*',
#             "Access-Control-Allow-Methods": 'GET,POST,PUT,DELETE,OPTIONS',
#             "Access-Control-Allow-Headers": 'Content-Type,Authorization'
#         }
#         return Response(status_code=200, headers=headers)
#     response = await call_next(request)
#     response.headers['Access-Control-Allow-Origin'] = '*'  # 允许所有源访问
#     return response


@app.get('/info')
async def get_info():
    return '内容成功获取!'


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main27:app', host="127.0.0.1", port=8000, reload=True)
