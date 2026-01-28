# ⚡ Projeto de Introdução - FastAPI | DDD | Clean Arch.

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

## 🤖 Automação de Usuários

### Geração de Usuários Aleatórios

O projeto inclui um sistema de automação inteligente para geração de usuários aleatórios através de web scraping:

#### `generate_user_scraper()`

Função que automatiza a geração de usuários aleatórios utilizando:

- **Selenium** + **undetected-chromedriver**: Automação de navegador que contorna detecção anti-bot
- **Brave Browser**: Navegador principal (configurável para Chrome)
- **Site gerador**: https://geradornv.com.br/

**Dados coletados:**
- Nome completo
- Data de nascimento
- Telefone celular
- Email

**Fluxo:**
```
1. Acessa gerador-pessoas → extrai nome e data de nascimento
2. Acessa gerador-celular → extrai número de telefone
3. Acessa gerador-email → extrai endereço de email
4. Formata e valida dados com helpers
5. Retorna objeto UserCreate pronto para persistência
```

### Helpers de Formatação

#### `BirthFormatter`
Formata datas de nascimento do padrão `DD/MM/YYYY` para objeto `date` Python:
```python
from app.helpers.birth_formatter import BirthFormatter
birth_date = BirthFormatter.format("15/03/1990")  # → date(1990, 3, 15)
```

#### `PhoneFormatter`
Formata números de telefone para o padrão brasileiro `(XX) XXXXX-XXXX`:
```python
from app.helpers.phone_formatter import PhoneFormatter
formatted = PhoneFormatter.format("11987654321")  # → "(11) 98765-4321"
```

### Requisitos para Automação

- **Navegador**: Brave Browser (ou Chrome) instalado no sistema
- **Python 3.11+**: Requerido para compatibilidade com undetected-chromedriver
- **Variáveis de Ambiente**: Opcional (caminho do navegador)

### Configuração

No arquivo `app/infra/generate_user.py`, você pode customizar:

```python
# Trocar para Chrome (comentar linha do Brave)
# options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Configurar modo headless
driver = uc.Chrome(options=options, headless=False)  # True para modo headless
```

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