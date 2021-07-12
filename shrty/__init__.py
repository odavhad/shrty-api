import os
from fastapi import FastAPI, HTTPException, status

from shrty import auth, schemas


app = FastAPI()

auth_handler = auth.AuthHandler()


@app.post("/auth", tags=["auth"])
def authorize_user(user: schemas.UserAuth):
    USERNAME = os.getenv("USER_NAME")

    if user.username != USERNAME:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"description": "invalid username."},
        )

    elif not auth_handler.verify(user.password):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail={"description": "invalid password."},
        )

    return auth_handler.encode_token(user.username)
