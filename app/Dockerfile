# Базовый образ Python
FROM python:3.12-slim

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование зависимостей и их установка
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остального кода приложения
COPY . .

# Открытие порта для работы приложения
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]