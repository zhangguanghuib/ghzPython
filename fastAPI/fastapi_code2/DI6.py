from fastapi import FastAPI, Depends
app = FastAPI()


class  UserService:
    def __init__(self,db_connection: str = "DefaultDBConnection"):
        self.db_connection = db_connection
    
    def get_user(self, user_id: int):
        return {"user_id": user_id, "name": "John Doe", "db_connection": self.db_connection}

def get_user_service():
    return UserService(db_connection='test-db')

@app.get("/users/{user_id}")
async def read_user(
    user_id: int, 
    user_service: UserService = Depends(get_user_service)
    ):
    return user_service.get_user(user_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("DI6:app",host='127.0.0.1',port=8000,reload=True)