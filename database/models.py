from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DetectionRecord(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True)
    objects = Column(String)
    labels = Column(String)