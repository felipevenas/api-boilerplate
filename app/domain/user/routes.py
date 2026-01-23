from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.domain.user.repository import UserRepository
from app.domain.user.service import UserService
from app.domain.user.schemas import UserRead, UserCreate, UserUpdate
from app.core.response import success_response, error_response

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repo = UserRepository(db)
    return UserService(repo)

@router.get("/users", response_model=dict, status_code=status.HTTP_200_OK, summary="Buscar todos os usuários")
def get_all(service: UserService = Depends(get_user_service)):
    """ Busca de todos os usuários cadastrados no banco de dados """
    users = service.get_all()
    if not users:
        return error_response("Ocorreu um erro ao buscar todos os usuários!", users)
    return success_response(users, "Usuários retornados com sucesso!")

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED, summary="Criar um novo usuário")
def post(data: UserCreate,
         service: UserService = Depends(get_user_service)):
    """ Cria um novo usuário no banco de dados """
    try:
        user = service.post(data)
        return success_response(user, "Novo usuário cadastrado com sucesso!")
    except ValueError as e:
        return error_response("Ocorreu um erro ao criar um novo usário!", details=str(e))