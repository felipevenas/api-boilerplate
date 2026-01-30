import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
import sys

LOG_DIR = Path(__file__).resolve().parents[3] / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "api.log"

file_handler = TimedRotatingFileHandler(
    str(LOG_FILE),
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8"
)

file_handler.suffix = "%Y-%m-%d"
file_handler.namer = lambda name: name if name.endswith(".log") else f"{name}.log"

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)

log_format = "%(asctime)s - [%(levelname)s] - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

formatter = logging.Formatter(log_format, datefmt=date_format)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger = logging.getLogger("api_logger")
if not logger.handlers:
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.propagate = False
    logger.info("✅ Sistema de Logging da API Configurado com Rotação Diária!")
