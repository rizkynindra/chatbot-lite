FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 212
ENV FLASK_APP=app.py
CMD ["python", "train.py"]
CMD ["flask", "run", "--host", "0.0.0.0"]