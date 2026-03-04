from app.domain.user.schemas import UserCreate
from app.helpers.birth_formatter import BirthFormatter as bf
from app.infra.logging.logger import logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import time
import random

def generate_user_scraper():
    options = uc.ChromeOptions()
    driver = uc.Chrome(
        version_main=144,
        options=options,
        headless=True # -> Automação roda em segundo-plano.
    )
    wait = WebDriverWait(driver, 30)
    url = "https://geradornv.com.br/"
    try:
        driver.get(f"{url}gerador-pessoas/")
        driver.maximize_window()
        logger.info(f"🛜 Inicializando navegador maximizado no site: {url}gerador-pessoas/...")
        time.sleep(3)
        name = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nv-field-name"]'))
        ).text
        logger.info(f"👤 Nome coletado com sucesso: {name}")
        time.sleep(3)
        birth = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nv-field-birthday"]'))
        ).text
        logger.info(f"📅 Data de nascimento coletada com sucesso: {birth}")
        driver.get(f"{url}gerador-celular/")
        logger.info(f"🛜 Trocando de seção no site: {url}gerador-celular/...")
        time.sleep(3)
        phone = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nv-field-generator-cellphone"]'))
        ).text
        logger.info(f"📱 Número de celular coletado com sucesso: {phone}")
        driver.get(f"{url}gerador-email/")
        logger.info(f"🛜 Trocando de seção no site: {url}gerador-email/...")
        time.sleep(3)
        email = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nv-field-generator-email"]'))
        ).text
        logger.info(f"✉️ E-mail coletado com sucesso: {email}")
        return UserCreate(
            name=name,
            email=email,
            phone=phone,
            birth=bf.format(birth),
            password=str(random.randint(100000, 1000000)) # Gera uma senha numérica aleatória
        )
    except ValueError as e:
        raise RuntimeError(f"Erro ao tentar copiar um número aleatório: {str(e)}")
    finally:
        logger.info(f"⏸️ Encerrando automação...")
        driver.quit()