from app.domain.user.repository import UserRepository
from app.domain.user.schemas import UserRead
from app.helpers.phone_formatter import PhoneFormatter as pf
from app.infra.scrapers.generate_user import generate_user_scraper
from app.infra.logging.logger import logger

class AutomationService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def generate_user(self) -> UserRead:
        """ Gera um novo usuário através de um Web Scraper """
        generated_user = generate_user_scraper()
        generated_user.phone = pf.format(generated_user.phone)
        logger.info(f"📱 [Domain/Automation] Telefone formatado com sucesso: {generated_user.phone}!")
        user_db = self.repo.post(generated_user)
        return UserRead.model_validate(user_db)