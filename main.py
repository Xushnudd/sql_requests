from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from typing import Optional

engine = create_engine("sqlite:///data.db", echo=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    bio: Mapped[Optional[str]]
    
Base.metadata.create_all(engine)
    
# with Session(engine) as session:
#     new_user = User(username="Asadbek", email="asadbek@examle.com", bio="Sevgidan kuygan chiyabo'ri")
#     session.add(new_user)
#     session.commit()

