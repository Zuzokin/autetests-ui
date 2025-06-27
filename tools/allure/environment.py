import sys
from config import settings
import platform


def create_allure_environment_file():
    # словарь environment.properties
    env_data = {
        **settings.model_dump(),  # Все настройки из конфига
        "os_info": f"{platform.system()}, {platform.release()}",
        "python_version": sys.version,
        "platform_architecture": platform.machine(),
    }
    # Создаем список из элементов в формате {key}={value}
    env_prop = [f'{key}={value}' for key, value in env_data.items()]
    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(env_prop)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+', encoding="utf-8") as file:
        file.write(properties)  # Записываем переменные в файл
