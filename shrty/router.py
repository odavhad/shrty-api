from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from shrty import auth, models, schemas
from shrty.database import get_db


auth_handler = auth.AuthHandler()
crud_router = APIRouter(
    prefix="/url", tags=["url"], dependencies=[Depends(auth_handler.auth_wrapper)]
)


@crud_router.post("")
def add_url(url: schemas.URLSchemaCreate, db: Session = Depends(get_db)):
    db_tag = (
        db.query(models.URLModel)
        .filter(models.URLModel.short_tag == url.short_tag)
        .first()
    )

    if not db_tag:
        db_url = models.URLModel(
            short_tag=url.short_tag,
            target_url=url.target_url,
            visit_count=url.visit_count,
            public=url.public,
        )

        db.add(db_url)
        db.commit()
        db.refresh(db_url)

        return db_url

    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"description": "the entered shortened tag is not unique."},
        )


@crud_router.get("/{url_id}")
def get_url(url_id: int, db: Session = Depends(get_db)):
    db_url = db.query(models.URLModel).filter(models.URLModel.id == url_id).first()

    if db_url:
        return db_url

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "description": "no item present in the database with the given url id."
            },
        )


@crud_router.put("/{url_id}")
def modify_url(
    url_id: int, url: schemas.URLSchemaModify, db: Session = Depends(get_db)
):
    db_url = db.query(models.URLModel).filter(models.URLModel.id == url_id).first()

    if db_url:
        if db_url.short_tag != url.short_tag:
            db_tag = (
                db.query(models.URLModel)
                .filter(models.URLModel.short_tag == url.short_tag)
                .first()
            )

            if db_tag:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail={"description": "the entered shortened tag is not unique."},
                )

        if not url.visit_count:
            url.visit_count = db_url.visit_count

        db.query(models.URLModel).filter(models.URLModel.id == url_id).update(
            {
                "short_tag": url.short_tag,
                "target_url": url.target_url,
                "visit_count": url.visit_count,
                "public": url.public,
            }
        )
        db.commit()

        db.refresh(db_url)

        return db_url

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "description": "no item present in the database with the given url id."
            },
        )


@crud_router.delete("/{url_id}")
def delete_url(url_id: int, db: Session = Depends(get_db)):
    db_url = db.query(models.URLModel).filter(models.URLModel.id == url_id).first()

    if db_url:
        db_url = (
            db.query(models.URLModel)
            .filter(models.URLModel.id == url_id)
            .delete(synchronize_session=False)
        )
        db.commit()

        return {"description": "delete successful."}

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "description": "no item present in the database with the given url id."
            },
        )
