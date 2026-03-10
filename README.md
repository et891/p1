## Запуск

### 1. Установить зависимости
pip install -r requirements.txt

### 2. Запустить сервер
uvicorn app.main:app --reload

### 3. Открыть Swagger
http://127.0.0.1:8000/docs