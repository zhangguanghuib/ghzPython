# 其响应
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get('/string1')
async def get_string1():
    return 'Hello World'  # Content-Type: text/plain


@app.get('/string2')
async def get_string2():
    return '<html><h1>Hello</h1></html>'


@app.get('/string3', response_class=HTMLResponse)
async def get_string3():
    return '<html><h1>Hello</h1></html>'


@app.get('/redirect1')
async def get_redirect1():
    return RedirectResponse(url='/string1')


@app.get('/items')
async def get_items(name: str):
    return {'name': name}


@app.get('/redirect2')
async def get_redirect2():
    return RedirectResponse(url='/items?name=Jack')

# 挂在HTML目录
app.mount('/html', StaticFiles(directory='templates', html=True))
app.mount('/static', StaticFiles(directory='static'))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main18:app', host='127.0.0.1', port=8000, reload=True)
