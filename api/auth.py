from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.models.user import User
from db.session import SessionLocal
from helper.auth import AuthHelper

router = APIRouter(prefix="/auth")
auth_helper = AuthHelper()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register_user(username: str, password: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.username == username).first()
        if user:
            raise HTTPException(status_code=400, detail="Username already exists")
        new_user = User(
            username=username, hashed_password=auth_helper.hash_password(password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/login")
def login_user(username: str, password: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="username not found")
        if not auth_helper.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid password")
        token = auth_helper.create_access_token(payload={"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
