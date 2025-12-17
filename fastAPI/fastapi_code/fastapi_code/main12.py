# 测试异步
from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

# 异步 endpoint：模拟并发 I/O 操作


@app.get("/async")
async def async_endpoint():
    start = time.time()
    # 模拟 5 次异步 I/O 操作（并发执行）
    tasks = [asyncio.sleep(1) for _ in range(5)]
    await asyncio.gather(*tasks)
    end = time.time()
    return {"异步时长": f"{end - start:.2f}秒"}

# 同步 endpoint：模拟相同的 I/O 操作


@app.get("/sync")
def sync_endpoint():
    start = time.time()
    # 模拟 5 次同步 I/O 操作（顺序执行）
    for _ in range(5):
        time.sleep(1)
    end = time.time()
    return {"同步时长": f"{end - start:.2f}秒"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main12:app', host="127.0.0.1", port=8000, reload=True)
