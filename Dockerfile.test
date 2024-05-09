# Используем базовый образ Alpine Linux
FROM python:alpine

# Установка зависимостей: numpy
RUN pip install numpy

# Копируем тестовый файл внутрь контейнера
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Команда для запуска тестов
CMD ["python", "-m", "unittest", "test_basic.py"]

