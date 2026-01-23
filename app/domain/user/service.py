from app.domain.user.repository import UserRepository
from app.domain.user.schemas import UserCreate, UserRead

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_all(self) -> list[UserRead]:
        """ Delega o repository para listar todos os usuários cadastrados no banco de dados """
        users = self.repo.get_all()
        return [UserRead.model_validate(u) for u in users]
    
    def post(self, data: UserCreate) -> UserRead:
        """ Delega o repository para criar um novo usuário no banco de dados """
        user = self.repo.post(data)
        return UserRead.model_validate(user)
