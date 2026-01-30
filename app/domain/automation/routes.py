from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.domain.user.repository import UserRepository
from app.domain.automation.services import AutomationService
from app.core.response import success_response, error_response

router = APIRouter()

def get_automation_service(db: Session = Depends(get_db)) -> AutomationService:
    repo = UserRepository(db)
    return AutomationService(repo)

@router.post("/automation/scraper/generate-user", status_code=status.HTTP_201_CREATED, summary="Automação que cria um usuário com dados aleatórios")
def generate_user(service: AutomationService = Depends(get_automation_service)):
    """ Automação que cria um usuário com dados aleatórios """
    user = service.generate_user()
    if not user:
        return error_response("Ocorreu um erro ao gerar um usuário aleatório!", user)
    return success_response(user, "Novo usuário gerado com sucesso!")