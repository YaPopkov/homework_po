### Руководство по запуску тестов

1. Создать виртуальное окружение (virtualenv Python 3.7+):
    ```
    virtualenv env 
    или
    virtualenv --python=C:\Python37\python.exe env 
    или
    python -m venv env
    или
    python3 -m venv env
   ```

2. Активировать виртуальное окружение, если необходимо:

    Точная команда зависит от среды разработки и ОС, например:
    ```
    . env/bin/activate
    или
    env\Scripts\activate
    ```
3. Установить зависимости:

    Для тестовой среды:
    
    ```
    pip install -r requirements.txt
    ```
4. Запустить тест:

    ```
   python -m pytest
   ```