from fastapi import FastAPI

from app.api.endpoints.routes import router as api_router
from app.core.config import get_settings
from app.infra.logging.logger import logger as infra_logger 

settings = get_settings()

app = FastAPI(
    title="Projeto - API Introduction",
    description=(
        "Essa API foi desenvolvida como um projeto introdutório para futuras soluções WEB."
        "Estão sendo utilizados a seguinte arquitetura de projeto: DDD e Clean Architeture"    
    ),
    contact={
        "name": "Felipe Venas | Desenvolvedor",
        "email": "felipevenas3003@gmail.com"
    },
    version="1.0.0",
    openapi_tags=[
        {"name": "Auth", "description": "Processos de autenticação do Usuário"},
        {"name": "User", "description": "Operações referentes aos Usuários"},
        {"name": "Automation", "description": "Automações gerais da API"}
    ]
)

logger = infra_logger 
logger.info("▶️ Aplicação iniciando...")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API está rodando perfeitamente!"}