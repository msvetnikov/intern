FROM python:3.12-slim
RUN pip install -r requirements.txt
COPY main.py /app/main.py
WORKDIR /app
EXPOSE 8000
ENV AUTHOR="Максим Светников"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
