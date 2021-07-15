import os
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session

from shrty import auth, models, router, schemas
from shrty.database import engine, get_db


models.Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="shrty/static"), name="static")


templates = Jinja2Templates(directory="shrty/templates")
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


@app.get("/")
def get_all_urls(request: Request, db: Session = Depends(get_db)):
    urls = (
        db.query(models.URLModel.short_tag, models.URLModel.target_url)
        .filter(models.URLModel.public == True)
        .order_by(models.URLModel.short_tag)
        .all()
    )

    return templates.TemplateResponse("index.html", {"request": request, "urls": urls})


@app.get("/json")
def get_all_urls(db: Session = Depends(get_db)):
    urls = (
        db.query(models.URLModel.short_tag, models.URLModel.target_url)
        .filter(models.URLModel.public == True)
        .order_by(models.URLModel.short_tag)
        .all()
    )

    return urls


@app.get("/stats", tags=["auth"])
def get_url_stats(
    db: Session = Depends(get_db), user: str = Depends(auth_handler.auth_wrapper)
):
    urls = db.query(models.URLModel).order_by(models.URLModel.short_tag).all()

    return urls


app.include_router(router.crud_router)


@app.get("/404")
def not_found(request: Request):
    return templates.TemplateResponse("404.html", {"request": request})


@app.get("/{short_tag}")
def route(short_tag: str, db: Session = Depends(get_db)):
    db_url = (
        db.query(models.URLModel).filter(models.URLModel.short_tag == short_tag).first()
    )

    print(db_url)

    if db_url:
        response = RedirectResponse(db_url.target_url)

        db.query(models.URLModel).filter(models.URLModel.short_tag == short_tag).update(
            {"visit_count": db_url.visit_count + 1}
        )
        db.commit()

        return response

    else:
        response = RedirectResponse("404")

        return response
