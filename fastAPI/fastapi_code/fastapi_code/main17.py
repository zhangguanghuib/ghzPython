# 文件响应

from fastapi import FastAPI
from fastapi.responses import Response, FileResponse, StreamingResponse
app = FastAPI()


@app.get('/download_file')
async def get_custom_file():
    info = b'File Content'
    return Response(
        content=info,
        media_type='text/plain',  # 文本内容
        # attachment 直接下载
        headers={'Content-Disposition': 'attachment;filename="file.txt"'}
    )


@app.get('/download_pdf')
async def get_custom_pdf():
    path = './data/fastapi文档.pdf'
    return FileResponse(
        path=path,
        media_type='application/pdf',  # PDF文件
        headers={'Content-Disposition': 'attachment;filename="file.pdf"'}
    )


def generate_chunks(file_path: str, chunk_size: int = 1024*1024*10):
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            yield chunk


@app.get('/download_mp4')
async def get_custom_mp4():
    path = './data/AI变声器.mp4'
    return StreamingResponse(
        content=generate_chunks(path),
        media_type='video/mp4',  # mp4文件
        headers={'Content-Disposition': 'attachment;filename="file.mp4"'}
    )
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main17:app', host="127.0.0.1", port=8000, reload=True)
