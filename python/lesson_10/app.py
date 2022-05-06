from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from database import SessionLocal
from table_user import User
from table_post import Post
from schema import UserGet, PostGet

app = FastAPI()

def get_db():
    with SessionLocal() as db:
        yield db


@app.get("/user/{id}", response_model=UserGet)
def get_user(id: int, db: Session = Depends(get_db)):
    try:
        return db.query(User).filter(User.id == id).one()
    except NoResultFound:
        raise HTTPException(404, detail="User not found")
    except:
        raise

@app.get("/post/{id}", response_model=PostGet)
def get_post(id: int, db: Session = Depends(get_db)):
    try:
        return db.query(Post).filter(Post.id == id).one()
    except NoResultFound:
        raise HTTPException(404, detail="Post not found")
    except:
        raise
