Trading Exchange

Установка виртуального окружения

Для того чтобы поднять виртуальное окружение необходим пакетный менеджер uv:

    pip install uv

Далее необходимо установить все зависимости и виртуальное окружение и активировать его:

    uv sync 
    для Linux/MacOS - source .venv/bin/activate
    для Windows - .\.venv\Scripts\activate
Теперь можно запустить локальный сервер:

    uvicorn main:app --reload

Для того чтобы активировать pre-commit необходимо ввести команду:

    pre-commit 
    
    