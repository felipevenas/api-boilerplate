# ⚡ Boilerplate - FastAPI | DDD | Clean Arch.

## 📖 Propósito

Este repositório foi desenvolvido como uma **base de conhecimento estruturada** para servir como referência na construção de futuras aplicações. É um **boilerplate profissional** que demonstra na prática:

### 🎯 Objetivos

- **Arquitetura Limpa (Clean Architecture)** - Separação clara de responsabilidades em camadas bem definidas
- **Domain-Driven Design (DDD)** - Organização por domínios de negócio, facilitando manutenção e escalabilidade
- **Padrões de Código** - Implementação de convenções e padrões reconhecidos na comunidade
- **Type Safety** - Uso de type hints e validação rigorosa de dados
- **Maintainability** - Código organizado, testável e fácil de estender
- **Async-First** - Operações assíncronas para melhor performance

### 🎓 O que você aprenderá

- Como estruturar um projeto FastAPI profissionalmente
- Padrão Repository para abstração de acesso a dados
- Padrão Service para lógica de negócio
- Validação robusta com Pydantic v2
- Configuração de banco de dados com SQLAlchemy 2.0
- Respostas padronizadas e tratamento de erros
- Variáveis de ambiente com dotenv

### 💡 Caso de Uso

Use este repositório como template quando precisar criar:
- APIs RESTful escaláveis
- Microserviços bem estruturados
- Aplicações que requerem boas práticas arquiteturais
- Projetos que necessitam de base sólida para crescimento futuro

> Uma API robusta e bem estruturada com padrões de desenvolvimento profisionais.

## 🏷️ Stack

| Tecnologia | Versão | Propósito |
|-----------|--------|----------|
| ![Python](https://img.shields.io/badge/Python-3.11+-3776ab?style=flat&logo=python) | 3.11+ | Linguagem principal |
| ![FastAPI](https://img.shields.io/badge/FastAPI-0.128.0-009688?style=flat&logo=fastapi) | 0.128.0 | Framework web |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.46-d32f2f?style=flat) | 2.0.46 | ORM |
| ![Pydantic](https://img.shields.io/badge/Pydantic-2.12.5-e92063?style=flat) | 2.12.5 | Validação de dados |
| ![MySQL](https://img.shields.io/badge/MySQL-asyncmy-4479a1?style=flat&logo=mysql) | asyncmy | Banco de dados |
| ![Selenium](https://img.shields.io/badge/Selenium-4.40.0-43B02A?style=flat&logo=selenium) | 4.40.0 | Web scraping |
| ![undetected-chromedriver](https://img.shields.io/badge/undetected--chromedriver-3.5.5-4285F4?style=flat) | 3.5.5 | Automação de navegador |

## 📁 Arquitetura

```
api-start/
├── app/
│   ├── api/
│   │   └── endpoints/
│   │       └── routes.py         # Rotas principais
│   ├── core/
│   │   ├── config.py             # Configurações da aplicação
│   │   └── response.py           # Modelos padrão de resposta
│   ├── db/
│   │   ├── base_class.py         # Classe base para modelos
│   │   └── session.py            # Configuração de sessão BD
│   ├── domain/
│   │   └── user/
│   │       ├── model.py          # Modelo SQLAlchemy
│   │       ├── repository.py     # Acesso aos dados
│   │       ├── routes.py         # Rotas da entidade
│   │       ├── schemas.py        # Schemas Pydantic
│   │       └── service.py        # Lógica de negócio
│   ├── helpers/                  # Utilitários (formatadores)
│   │   ├── birth_formatter.py    # Formatação de data de nascimento
│   │   └── phone_formatter.py    # Formatação de telefone
│   └── infra/                    # Infraestrutura
│       └── generate_user.py      # Automação de geração de usuários
├── requeriments.txt              # Dependências
└── README.md                      # Este arquivo
```

## 🏗️ Padrão de Arquitetura

A aplicação segue o padrão **Clean Architecture** com separação de responsabilidades:

### Camadas

```
┌─────────────────────────────────────┐
│      API / Routes (Endpoints)       │  ← Requisições HTTP
├─────────────────────────────────────┤
│        Service (Lógica)             │  ← Regras de negócio
├─────────────────────────────────────┤
│     Repository (Persistência)       │  ← Acesso ao BD
├─────────────────────────────────────┤
│   Models + Database Session         │  ← BD
└─────────────────────────────────────┘
```

### Domain-Driven Design

Cada entidade (ex: `user`) possui:
- **model.py** - Definição do modelo de dados (SQLAlchemy)
- **schemas.py** - Schemas de validação (Pydantic)
- **repository.py** - Operações de persistência
- **service.py** - Lógica de negócio
- **routes.py** - Endpoints HTTP

## 🚀 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
DB_NAME=sua_base_dados
```

### Instalação

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instalar dependências
pip install -r requeriments.txt
```

## 📦 Dependências Principais

```
fastapi==0.128.0              # Framework web assíncrono
SQLAlchemy==2.0.46            # ORM para BD
pydantic==2.12.5              # Validação de dados
python-dotenv==1.2.1          # Carregamento de variáveis
starlette==0.50.0             # ASGI framework
uvicorn==0.40.0               # Servidor ASGI
selenium==4.40.0              # Automação de navegador
undetected-chromedriver==3.5.5 # Chrome driver anti-detecção
requests==2.32.5              # Requisições HTTP
```

## 🐋 Docker & Containerização

### Sobre a Infraestrutura de Containers

O projeto utiliza **Docker Compose** para orquestrar os containers necessários:

#### Serviços

| Serviço | Imagem | Porta | Propósito |
|---------|--------|-------|----------|
| **MySQL** | `mysql:8.0` | 3306 | Banco de dados relacional |
| **phpMyAdmin** | `phpmyadmin` | 8080 | Interface web para gerenciamento do BD |

#### Arquivo `docker-compose.yml`

```yaml
version: '3.9'

services:
  mysql:
    image: mysql:8.0
    container_name: mysql_local
    restart: unless-stopped
    ports:
      - "${DB_PORT}:3306"
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_PASS}
      MYSQL_DATABASE: ${DB_NAME}
      MYSQL_ALLOW_EMPTY_PASSWORD: "yes"
    volumes:
      - mysql_data:/var/lib/mysql

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: phpmyadmin
    restart: unless-stopped
    ports:
      - "8080:80"
    environment:
      PMA_HOST: mysql
      PMA_PORT: 3306
    depends_on:
      - mysql

volumes:
  mysql_data:
```

### Executar Containers

```bash
# Iniciar containers em background
docker-compose up -d --build

# Visualizar status dos containers
docker-compose ps

# Ver logs de um serviço específico
docker-compose logs -f mysql
docker-compose logs -f phpmyadmin

# Parar containers
docker-compose down

# Remover volumes (dados) também
docker-compose down -v
```

### Acessar Serviços

- **MySQL**: `localhost:3306` (via ferramentas como DBeaver, MySQL Workbench)
- **phpMyAdmin**: `http://localhost:8080`
  - Usuário: `root`
  - Senha: valor de `DB_PASS` no `.env`

### Variáveis de Ambiente para Docker

Adicione ao arquivo `.env`:

```env
# Docker - MySQL
DB_USER=root
DB_PASS=sua_senha_aqui
DB_HOST=localhost
DB_PORT=3306
DB_NAME=seu_banco_aqui
```

> **Nota**: Quando usar containers, `DB_HOST=mysql` (nome do serviço). Quando usar BD local, `DB_HOST=localhost`.

## 💾 Configuração do Banco de Dados

### Conexão (session.py)

```python
DATABASE_URL = f"mysql+asyncmy://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
```

## 🔄 Fluxo de Requisição

```
1. Request HTTP
   ↓
2. Router → Validação (Pydantic/Schemas)
   ↓
3. Service → Lógica de Negócio
   ↓
4. Repository → Operação no BD
   ↓
5. Response → Padrão unificado (response.py)
```

## 💉 Injeção de Dependência (Dependency Injection)

O projeto utiliza o sistema de injeção de dependência do FastAPI através da função `Depends()`. Isso permite:

- ✅ Desacoplamento de componentes
- ✅ Facilita testes unitários
- ✅ Código mais limpo e manutenível
- ✅ Reutilização de lógica comum

### Padrão Implementado

**Exemplo - Domínio User:**

```python
# 1. Factory Function (cria e injeta dependências)
def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repo = UserRepository(db)
    return UserService(repo)

# 2. Route recebe o serviço injetado
@router.get("/users")
def get_all(service: UserService = Depends(get_user_service)):
    return service.get_all()
```

**Exemplo - Domínio Automation:**

```python
# 1. Factory Function específica da automação
def get_automation_service(db: Session = Depends(get_db)) -> AutomationService:
    repo = UserRepository(db)
    return AutomationService(repo)

# 2. Route recebe o serviço injetado
@router.post("/automation/scraper/generate-user")
def generate_user(service: AutomationService = Depends(get_automation_service)):
    return service.generate_user()
```

### Benefícios

| Aspecto | Benefício |
|--------|----------|
| **Testabilidade** | Mock de dependências fica trivial |
| **Escalabilidade** | Adicionar novos domínios segue o mesmo padrão |
| **Manutenibilidade** | Mudanças em uma camada não afetam outras |
| **Flexibilidade** | Trocar implementações sem alterar rotas |



## 📋 Padrão de Resposta

### Sucesso
```json
{
  "status": "success",
  "message": "Resposta obtida com sucesso!",
  "data": { }
}
```

### Erro
```json
{
  "status": "error",
  "message": "Ocorreu um erro!",
  "details": null
}
```

## 🛠️ Desenvolvimento

### Adicionar Nova Entidade

1. Criar pasta em `app/domain/{entidade}/`
2. Implementar `model.py` (SQLAlchemy)
3. Implementar `schemas.py` (Pydantic)
4. Implementar `repository.py` (CRUD)
5. Implementar `service.py` (Lógica)
6. Implementar `routes.py` (Endpoints)
7. Registrar rotas em `app/api/endpoints/routes.py`

## 🤖 Domínio de Automação - Geração de Usuários

### Visão Geral

O projeto inclui um **domínio dedicado de automação** (`app/domain/automation/`) que implementa geração inteligente de usuários aleatórios através de web scraping. Este sistema demonstra como adicionar funcionalidades avançadas mantendo a Clean Architecture.

### Estrutura do Domínio

```
app/domain/automation/
├── routes.py      # Endpoints HTTP da automação
├── services.py    # Lógica de geração de usuários
└── __pycache__/
```

### Arquitetura da Automação

#### 1. **Camada de Rota** (`routes.py`)

```python
@router.post("/automation/scraper/generate-user", 
             status_code=status.HTTP_201_CREATED, 
             summary="Automação que cria um usuário com dados aleatórios")
def generate_user(service: AutomationService = Depends(get_automation_service)):
    """Automação que cria um usuário com dados aleatórios"""
    user = service.generate_user()
    if not user:
        return error_response("Ocorreu um erro ao gerar um usuário aleatório!", user)
    return success_response(user, "Novo usuário gerado com sucesso!")
```

**Injeção de Dependência:**
```python
def get_automation_service(db: Session = Depends(get_db)) -> AutomationService:
    repo = UserRepository(db)
    return AutomationService(repo)
```

#### 2. **Camada de Serviço** (`services.py`)

```python
class AutomationService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def generate_user(self) -> UserRead:
        """Gera um novo usuário através de um Web Scraper"""
        generated_user = generate_user_scraper()
        generated_user.phone = pf.format(generated_user.phone)
        user_db = self.repo.post(generated_user)
        return UserRead.model_validate(user_db)
```

#### 3. **Camada de Infraestrutura** (`infra/scrapers/generate_user.py`)

Utiliza Selenium + undetected-chromedriver para contornar proteções anti-bot.

### Fluxo de Geração de Usuários

```
┌──────────────────────────────────────────────────────────┐
│  POST /automation/scraper/generate-user                  │
└────────────────────┬─────────────────────────────────────┘
                     ↓
        ┌────────────────────────────┐
        │  AutomationService         │
        │  ↓ get_automation_service()│
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │  generate_user_scraper()   │
        │  ↓ Acessa 3 sites:         │
        │    - gerador-pessoas       │
        │    - gerador-celular       │
        │    - gerador-email         │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │  Formatação de Dados       │
        │  - PhoneFormatter          │
        │  - BirthFormatter          │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │  UserRepository.post()     │
        │  ↓ Persistência no BD      │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │  Response (UserRead)       │
        │  ✅ Sucesso                │
        └────────────────────────────┘
```

### Geração de Usuários Aleatórios

#### `generate_user_scraper()`

Função que automatiza a geração de usuários aleatórios:

**Tecnologias:**
- **Selenium**: Automação de navegador
- **undetected-chromedriver**: Contorna detecção anti-bot
- **Brave Browser** (ou Chrome): Navegador executado

**Dados Coletados:**
- ✅ Nome completo
- ✅ Data de nascimento (DD/MM/YYYY)
- ✅ Telefone celular
- ✅ Email

**Sites Utilizados:**
- https://geradornv.com.br/ - Gerador de pessoas (nome + data de nascimento)
- https://geradornv.com.br/ - Gerador de celular
- https://geradornv.com.br/ - Gerador de email

### Helpers de Formatação

#### `PhoneFormatter`

Formata números de telefone para o padrão brasileiro `(XX) XXXXX-XXXX`:

```python
from app.helpers.phone_formatter import PhoneFormatter as pf

# Exemplo
formatted = pf.format("11987654321")  # → "(11) 98765-4321"
```

#### `BirthFormatter`

Formata datas de nascimento do padrão `DD/MM/YYYY` para objeto `date` Python:

```python
from app.helpers.birth_formatter import BirthFormatter

# Exemplo
birth_date = BirthFormatter.format("15/03/1990")  # → date(1990, 3, 15)
```

### Requisitos Técnicos

| Requisito | Versão | Observação |
|-----------|--------|-----------|
| Python | 3.11+ | Requerido para compatibilidade com undetected-chromedriver |
| Brave Browser ou Chrome | - | Deve estar instalado no sistema |
| Selenium | 4.40.0+ | Instalado via `requirements.txt` |
| undetected-chromedriver | 3.5.5+ | Contorna proteções anti-bot |

### Configuração e Customização

Arquivo: `app/infra/scrapers/generate_user.py`

```python
# Modo headless (sem interface gráfica)
driver = uc.Chrome(options=options, headless=True)   # True = headless
```

### Exemplo de Uso

```bash
# Iniciar a API
uvicorn app.main:app --reload

# Chamar o endpoint via curl
curl -X POST "http://localhost:8000/automation/scraper/generate-user"

# Ou usar o cliente HTTP (Swagger)
# Acesse: http://localhost:8000/docs
# Procure por: /automation/scraper/generate-user
```

### Resposta de Sucesso

```json
{
  "status": "success",
  "message": "Novo usuário gerado com sucesso!",
  "data": {
    "id": 1,
    "name": "João da Silva",
    "birth_date": "1990-03-15",
    "phone": "(11) 98765-4321",
    "email": "joao.silva@example.com"
  }
}
```

### Boas Práticas da Automação

✅ **Fazer:**
- Usar undetected-chromedriver para evitar bloqueios
- Configurar timeouts apropriados
- Implementar retry logic para falhas temporárias
- Logar operações importantes

❌ **Evitar:**
- Fazer requisições muito rápidas (respeitar rate limiting)
- Usar dados scrapeados para fins ilícitos
- Acessar dados sem consentimento
- Ignorar robots.txt e termos de serviço

### Limitações Conhecidas

⚠️ A automação depende de:
- Disponibilidade dos sites geradores
- Estructura HTML dos sites (mudanças quebram o scraper)
- Navegador Brave/Chrome instalado e atualizado
- Conexão de internet estável

## 📝 Convenções

- **Variáveis de Ambiente**: `SNAKE_CASE`
- **Nomes de Classes**: `PascalCase`
- **Nomes de Funções**: `snake_case`
- **Nomes de Arquivos**: `snake_case`
- **Imports**: Organizados por: stdlib → terceiros → locais

## 🔐 Boas Práticas

- ✅ Usar type hints em todas as funções
- ✅ Validar dados com Pydantic
- ✅ Usar async/await quando possível
- ✅ Manter lógica separada por camadas
- ✅ Documentar funções complexas
- ✅ Usar variáveis de ambiente para secrets

## 📚 Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0](https://docs.sqlalchemy.org/)
- [Pydantic v2](https://docs.pydantic.dev/latest/)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

---

**Desenvolvido com ❤️**
