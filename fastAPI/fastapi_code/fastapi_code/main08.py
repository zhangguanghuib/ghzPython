# 查询参数Query
from fastapi import FastAPI, Query

app = FastAPI()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main08:app', host="127.0.0.1", port=8000, reload=True)
