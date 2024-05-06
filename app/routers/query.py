from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.persistence.database import get_db
from app.persistence.models import Uri as UriModel
from app.web.schemas import *


router = APIRouter(
    prefix='/api/v1/url',
    tags=['query']
)

@router.get("/shortUrl/{short_url}", response_model=GetLongUriRes)
async def get_longurl(short_url: str,
                      db: Session = Depends(get_db)):
    existing_uri = db.query(UriModel).filter(UriModel.short_uri == short_url).first()

    if existing_uri is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return existing_uri