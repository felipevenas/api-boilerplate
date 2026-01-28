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

@router.get("/users", status_code=status.HTTP_200_OK, summary="Buscar todos os usuários")
def get_all(service: UserService = Depends(get_user_service)):
    """ Busca de todos os usuários cadastrados no banco de dados """
    users = service.get_all()
    if not users:
        return error_response("Ocorreu um erro ao buscar todos os usuários!", users)
    return success_response(users, "Usuários retornados com sucesso!")

@router.post("/", status_code=status.HTTP_201_CREATED, summary="Criar um novo usuário")
def post(data: UserCreate,
         service: UserService = Depends(get_user_service)):
    """ Cria um novo usuário no banco de dados """
    try:
        created_user = service.post(data)
        return success_response(created_user, "Novo usuário cadastrado com sucesso!")
    except ValueError as e:
        return error_response("Ocorreu um erro ao criar um novo usário!", details=str(e))
    
@router.get("/user/{id}", status_code=status.HTTP_200_OK, summary="Buscar um usuário pelo ID")
def get_by_id(id: int,
              service: UserService = Depends(get_user_service)):
    """ Busca um usuário através do seu ID """
    user = service.get_by_id(id)
    if not user:
        return error_response("Ocorreu um erro ao buscar o usuário!", user)
    return success_response(user, "Usuário encontrado com sucesso!")

@router.put("/user/{id}", status_code=status.HTTP_200_OK, summary="Alterar dados de um usuário pelo ID")
def put(id: int,
        data: UserUpdate,
        service: UserService = Depends(get_user_service)):
    """ Alterar dados de um usuário pelo ID """
    try:
        updated_user = service.put(id, data)
        return success_response(updated_user, "Dados do usuário alterados com sucesso!")
    except ValueError as e:
        return error_response("Ocorreu um erro ao alterar os dados do usuário!", details=str(e))
    
@router.delete("/user/{id}", status_code=status.HTTP_200_OK, summary="Deleta um usuário pelo ID")
def delete(id: int,
           service: UserService = Depends(get_user_service)):
    """ Deleta um usuário pelo ID """
    deleted_user = service.delete(id)
    if not deleted_user:
        return error_response("Ocorreu um erro ao deletar o usuário!", deleted_user)
    return success_response(deleted_user, "Usuário deletado com sucesso!")

@router.post("/user/generate-user", status_code=status.HTTP_201_CREATED, summary="Automação que cria um usuário com dados aleatórios")
def generate_user(service: UserService = Depends(get_user_service)):
    """ Automação que cria um usuário com dados aleatórios """
    user = service.generate_user()
    if not user:
        return error_response("Ocorreu um erro ao gerar um usuário aleatório!", user)
    return success_response(user, "Novo usuário gerado com sucesso!")