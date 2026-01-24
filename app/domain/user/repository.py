from sqlalchemy.orm import Session
from sqlalchemy.future import select
from datetime import datetime

from app.domain.user.schemas import UserUpdate
from app.domain.user.model import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_all(self) -> list[User]:
        """ Lista todos os usuários do banco de dados através de um SELECT """
        result = self.db.execute(select(User))
        return result.scalars().all()
    
    def post(self, data) -> User:
        """ Cria um novo usuário no banco de dados """
        user = User(
            name=data.name,
            email=data.email,
            phone=data.phone,
            birth=data.birth,
            active=True,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        self.db.add(user)
        self.db.commit()
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