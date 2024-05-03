# Використовуємо базовий образ Python версії 3.11
FROM python:3.11

# Копіюємо ваші файли у робочу директорію контейнера
COPY . /app

# Встановлюємо робочу директорію
WORKDIR /app

# Команда, що виконує вашу програму при запуску контейнера
CMD ["python", "main.py"]