# logging_config.py

import logging
from logging.handlers import RotatingFileHandler
import logging
from logging.handlers import RotatingFileHandler
from io import TextIOWrapper
import os
import sys
import codecs

# Настройка кодировки для stdout и stderr
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer)
def setup_logging(file_name:str="app.log"):
    # Создаем директорию для логов, если её нет
    log_dir = 'log'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Настройка корневого логгера
    logger = logging.getLogger()    
    logger.setLevel(logging.DEBUG)  # Устанавливаем минимальный уровень логирования

    # Форматировщик для логов
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Файловый обработчик с ротацией
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, file_name),
        maxBytes=10485760 ,  # 10 Мб
        backupCount=10,   # Сохранять 10 резервных копий
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)  # Уровень логирования для файла

     # Консольный обработчик
    try:
        # Проверяем, есть ли атрибут buffer
        if hasattr(sys.stdout, 'buffer'):
            wrapped_stdout = TextIOWrapper(
                sys.stdout.buffer, 
                encoding='utf-8',  # указываем нужную кодировку
                errors='replace'  # обработка ошибок кодирования
            )
        else:
            wrapped_stdout = sys.stdout

        console_handler = logging.StreamHandler(wrapped_stdout)
    except Exception as e:
        # Если что-то пошло не так, используем стандартный StreamHandler
        console_handler = logging.StreamHandler()
        print(f"Ошибка при настройке консольного логгера: {e}")

    # console_handler = logging.StreamHandler(sys.stdout)
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.INFO)  # Уровень логирования для консоли
    

    # Добавляем обработчики к логгеру
    logger.addHandler(file_handler)
    
    # logger.addHandler(console_handler)

    # Опциональная настройка SQLAlchemy логирования
    sql_logger = logging.getLogger('sqlalchemy.engine')
    sql_logger.setLevel(logging.WARNING)
    sql_logger.addHandler(file_handler)

    return logger