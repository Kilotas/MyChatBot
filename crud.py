from sqlalchemy.orm import Session
import models

def save_message(db: Session, user_id: int, user_message: str, bot_response: str):
    message = models.Message(
        user_id=user_id,
        user_message=user_message,
        bot_response=bot_response
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message
