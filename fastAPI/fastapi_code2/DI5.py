from fastapi import FastAPI, Depends, HTTPException, Header, Request



app = FastAPI()

async def verify_token(token:str = Header(...)):
    if token != 'secret_key':
        raise HTTPException(status_code=403,detail='Invalid token')
    return token


async def get_current_user(token:str = Depends(verify_token)):
    return {'user':'admin','token':token}

@app.get("/user/")
async def get_user(user:dict = Depends(get_current_user)):
    return user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("DI5:app",host='127.0.0.1',port=8000,reload=True)