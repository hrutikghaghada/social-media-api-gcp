from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas, utils
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user_credentials: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user_credentials.password)
    user_credentials.password = hashed_password

    user = db.query(models.User).filter(
        models.User.email == user_credentials.email).first()

    if user is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"user with email: {user.email} already exists")

    new_user = models.User(**user_credentials.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id: {id} does not exist")

    return user
