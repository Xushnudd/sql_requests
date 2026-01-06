from sqlalchemy import create_engine, select
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
    
with Session(engine) as session:
    new_user = User(username="Asadbek", email="asadbek@examle.com", bio="Yana bir chiyabo'ri")
    session.add(new_user)
    session.commit()

with Session(engine) as session:
    read = session.execute(select(User)).scalars().all()
    for i in read:
        print(i.email, i.username, i.bio)
        
    stmt = select(User).where(User.username == "Asadbek")
    user = session.execute(stmt).scalar_one_or_none()
    
    