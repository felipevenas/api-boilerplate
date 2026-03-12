from sqlalchemy.orm import Session
from sqlalchemy.future import select
from datetime import datetime

from app.domain.user.schemas import UserUpdate
from app.domain.user.models import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> list[User]:
        """ Lista todos os usuários do banco de dados através de um SELECT """
        result = self.db.execute(select(User)
                                 .filter(User.active == True))
        return result.scalars().all()
    
    def post(self, data) -> User:
        """ Cria um novo usuário no banco de dados """
        user = User(
            name=data.name,
            email=data.email,
            username=data.username,
            password=data.password,
            phone=data.phone,
            birth=data.birth,
            active=True,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_by_id(self, id) -> User:
        """ Busca um usuário através do seu ID """
        result = self.db.execute(select(User).where(User.id == id))
        return result.scalars().first()
    
    def put(self, id, data: UserUpdate) -> User:
        """ Atualiza os dados do usuário encontrado pelo seu ID """
        user = self.get_by_id(id)
        if user:
            user.name = data.name
            user.email = data.email
            user.phone = data.phone
            user.birth = data.birth
            user.active = data.active
            user.updated_at = datetime.now()
            self.db.commit()
            self.db.refresh(user)
            return user
        
    def delete(self, id):
        """ Delete um usuário através do seu ID """
        user = self.get_by_id(id)
        self.db.delete(user)
        self.db.commit()
        return user
    
    def get_by_email(self, email: str) -> User | None:
        """ Busca um usuário através do seu E-mail """
        result = self.db.execute(select(User).where(User.email == email))
        return result.scalars().first()

    def get_by_username(self, username: str) -> User | None:
        """ Busca um usuário através do seu Username """
        result = self.db.execute(select(User).where(User.username == username))
        return result.scalars().first()
    
    def active(self, id: int) -> User:
        """ Ativa ou inativa um Usuário através do seu ID """
        user = self.get_by_id(id)
        if user:
            if user.active == True:
                user.active = False
            else:
                user.active = True
            self.db.commit()
            self.db.refresh(user)
            return user