# 文件上传
# pip install aiofiles==24.1.0
from pathlib import Path

from fastapi import FastAPI, File, UploadFile, HTTPException, Form
import aiofiles

app = FastAPI()


@app.post("/upload1/")
def upload_file1(file: bytes = File(...)):
    with open('./data/file.jpg', 'wb') as f:
        f.write(file)
    return {"msg": "文件上传成功"}


@app.post('/upload2/')
async def upload_file2(file: UploadFile):
    async with aiofiles.open(f'./data/{file.filename}', 'wb') as f:
        # chunk = await file.read(1024*1024)
        # while chunk:
        #     await f.write(chunk)
        #     chunk = await file.read(1024*1024)

        while chunk := await file.read(1024*1024):  # 分块读取1MB
            await f.write(chunk)

    return {"msg": "文件上传成功"}


@app.post('/batch-upload/')
def batch_upload(files: list[UploadFile] = File(...)):
    '''批量上传文件'''
    return {"count": len(files), "names": [f.filename for f in files]}


# 限制上传格式
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.gif'}


@app.post('/upload-image/')
def upload_image(file: UploadFile):
    '''限制上传格式'''
    # 验证文件格式
    ext = Path(file.filename).suffix.lower()
    print('='*20, ext)
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, '不支持的文件扩展名')
    # 保存文件的逻辑
    return {"msg": "文件上传成功"}


@app.post('/submit-form')
def submit_form(uname: str = Form(...),
                file: UploadFile = File(...)):
    return {"uname": uname, "filename": file.filename}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main13:app', host="127.0.0.1", port=8000, reload=True)
