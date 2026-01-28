from app.domain.user.schemas import UserCreate
from app.helpers.birth_formatter import BirthFormatter as bf

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
import time

def generate_user_scraper():
    options = uc.ChromeOptions()
    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" # Se tiver o Chrome instalado, comente essa linha.
    driver = uc.Chrome(
        options=options,
        headless=False
    )
    wait = WebDriverWait(driver, 30)
    url = "https://geradornv.com.br/"
    try:
        driver.get(f"{url}gerador-pessoas/")
        driver.maximize_window()
        time.sleep(3)
        name = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nv-field-name"]'))
        ).text
        time.sleep(3)
        birth = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nv-field-birthday"]'))
        ).text
        driver.get(f"{url}gerador-celular/")
        time.sleep(3)
        phone = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nv-field-generator-cellphone"]'))
        ).text
        driver.get(f"{url}gerador-email/")
        time.sleep(3)
        email = wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="nv-field-generator-email"]'))
        ).text
        return create_user(
            name=name,
            email=email,
            phone=phone,
            birth=bf.format(birth)
        )
    except ValueError as e:
        raise RuntimeError(f"Erro ao tentar copiar um número aleatório: {str(e)}")
    finally:
        driver.quit()

def create_user(name, email, phone, birth):
    return UserCreate(
        name=name,
        email=email,
        phone=phone,
        birth=birth
    )