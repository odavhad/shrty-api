import os
import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime, timedelta


class AuthHandler:
    security = HTTPBearer()
    SECRET_KEY = os.getenv("SECRET_KEY")

    def verify(self, password):
        PASSWORD = os.getenv("PASSWORD")

        return password == PASSWORD

    def encode_token(self, username):
        payload = {
            "exp": datetime.utcnow() + timedelta(minutes=5),
            "iat": datetime.utcnow(),
            "user": username,
        }

        return jwt.encode(payload, self.SECRET_KEY, algorithm="HS256")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=["HS256"])
            return payload["user"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail={"decription": "access token has expired."},
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"decription": "access token is invalid."},
            )

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)
