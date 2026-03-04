from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.domain.auth.schemas import RegisterRequest, TokenResponse
from app.core.auth import hash_password, verify_password, create_access_token
from app.domain.user.repository import UserRepository
from app.domain.user.services import UserService
from app.domain.user.schemas import UserCreate
from app.api.auth.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter()

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repo = UserRepository(db)
    return UserService(repo)

@router.get("/me")
def me(current_user=Depends(get_current_user)):
    return current_user

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(
    data: RegisterRequest,
    service: UserService = Depends(get_user_service),
):
    exists = service.get_by_email(data.email)
    if exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="E-mail ja cadastrado.",
        )

    user = UserCreate(
        name=data.name,
        email=data.email,
        username=data.username,
        password=hash_password(data.password),
        phone=data.phone,
        birth=data.birth,
    )
    return service.post(user)

@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(get_user_service),
):
    user = service.get_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais invalidas.",
        )
    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario inativo.",
        )
    token = create_access_token(sub=str(user.id))
    return TokenResponse(access_token=token)
