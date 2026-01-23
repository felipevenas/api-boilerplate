from fastapi import FastAPI, Request, HTTPException
import uvicorn

from app.api.endpoints.routes import router as api_router
from app.core.config import get_settings

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
        {"name": "Users", "description": "Operações referentes aos Usuários"}
    ]
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API está rodando perfeitamente!"}