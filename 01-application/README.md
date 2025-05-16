**FastAPI-приложение** (`main.py`):
- Получение имени хоста `socket.gethostname()`
- Получение IP клиента `request.client.host`
- Получение переменной `AUTHOR` (по умолчанию `"Unknown"`)
- Возвращает JSON с полями `hostname`, `ip_address`, `author`

**Dockerfile**:
- Базовый образ: `python:3.12-slim`
- Копирование `main.py` и установка зависимостей из `requirements.txt`
- Открытие порта 8000 и установка ENV-переменной `AUTHOR="Максим Светников"`

Команды для сборки и пуша образа в приватный репозиторий (приватный репозитроий создан через web интерфейс)
Вход в Docker Hub:
```bash
docker login
```
Сборка образа с тегом:
```bash
docker build -t msvetnikov/intern:2.0 .
```
Пуш в приватный репозиторий:
```bash
docker push msvetnikov/intern:2.0
```