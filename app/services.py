from typing import List

from sqlalchemy.orm import Session

from app.database import Base


class QueryService:

    def get_by_id(self, db: Session, model: Base, id: str):
        return db.query(model).get(id)

    def save(self, db: Session, obj: Base):
        db.add(obj)
        db.commit()
        db.refresh(obj)

        return obj

    def bulk_save(self, db: Session, objects: List[Base]):
        db.bulk_save_objects(objects)
        db.commit()

    def update(self, db: Session):
        db.commit()
