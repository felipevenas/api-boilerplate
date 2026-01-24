from app.domain.user.repository import UserRepository
from app.domain.user.schemas import UserCreate, UserRead, UserUpdate
from app.helpers.phone_formatter import PhoneFormatter as pf

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_all(self) -> list[UserRead]:
        """ Lista todos os usuários do banco de dados """
        users = self.repo.get_all()
        return [UserRead.model_validate(u) for u in users]
    
    def post(self, data: UserCreate) -> UserRead:
        """ Cria um novo usuário no banco de dados """
        data.phone = pf.format(data.phone)
        created_user = self.repo.post(data)
        return UserRead.model_validate(created_user)

    def get_by_id(self, id: int) -> UserRead:
        """ Busca um usuário através do seu ID """
        user = self.repo.get_by_id(id)
        return UserRead.model_validate(user)
    
    def put(self, id: int, data: UserUpdate) -> UserRead:
        """ Atualiza os dados de um usuário """
        updated_user = self.repo.put(id, data)
        return UserRead.model_validate(updated_user)
    
    def delete(self, id: int) -> UserRead:
        """ Deleta um usuário através do seu ID """
        deleted_user = self.repo.delete(id)
        return UserRead.model_validate(deleted_user)
