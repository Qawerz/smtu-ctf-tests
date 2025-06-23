from typing import Optional, List
from fastapi import APIRouter, Depends, Response
from config.settings import auth, config

from authx import RequestToken

from .schema import UserLoginSchema

app = APIRouter(prefix='/api/v1/auth', tags=["Аутентификация"])

@app.post("/login")
def login(
        data:UserLoginSchema, 
        responce: Response
    ):
    if data.name == "admin" and data.password == "123":
        token = auth.create_access_token(uid=data.name)
        return {"acess_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")

@app.get("/protected", dependencies=[Depends(auth.get_token_from_request)])
def get_protected(token: RequestToken = Depends()):
     try:
          auth.verify_token(token=token)
          return {"message": "Hello world !"}
     except Exception as e:
          raise HTTPException(401, detail={"message": str(e)}) from e