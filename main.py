from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from chat_gpt import get_gemini_response
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency для БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/chat", response_model=schemas.ChatResponse)
def chat(request: schemas.ChatRequest, db: Session = Depends(get_db)):
    try:
        bot_reply = get_gemini_response(request.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    crud.save_message(db, request.user_id, request.message, bot_reply)
    return {"response": bot_reply}
