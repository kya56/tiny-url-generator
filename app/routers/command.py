from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.persistence.database import get_db
from app.persistence.models import Uri as UriModel
from app.web.schemas import *
from app.domain.uri_shortener import UriShortener


router = APIRouter(
    prefix='/api/v1/url',
    tags=['command']
)

@router.post("/shorten", response_model=GetShortenUriRes)
async def get_tinyurl(req: GetShortenUriReq,
                      uri_shortener: UriShortener = Depends(UriShortener),
                      db: Session = Depends(get_db)):
    existing_uri = db.query(UriModel).filter(UriModel.long_uri == req.uri).first()

    if existing_uri is None:
        if uri_shortener:
            uri_obj = uri_shortener.shorten()
            db_entry = UriModel(id=uri_obj.id, long_uri=req.uri, short_uri=uri_obj.uri)
            db.add(db_entry)
            db.commit()
            return db_entry
        else:
            raise HTTPException(status_code=400, detail="Invalid url")
    else:
        return existing_uri