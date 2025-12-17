# Request获取请求信息

from fastapi import FastAPI, Request

app = FastAPI()


@app.get('/client-info')
async def client_info(request: Request):
    return {
        "请求URL": request.url,
        "请求方法": request.method,
        "请求IP": request.client.host,
        "请求参数": request.query_params,
        "请求头": request.headers,
        # "请求json": await request.json(),
        "请求cookies": request.cookies,
        # "请求form": await request.form(),
        # "请求files": request.files,
        "请求path_params": request.path_params,

    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main14:app', host='127.0.0.1', port=8000, reload=True)
