FROM python:3.13.12

RUN mkdir /app

WORKDIR /app

COPY requirements-pro.txt requirements-pro.txt

RUN pip install -r requirements-pro.txt

COPY routes/ routes/
COPY services/ services/
COPY config.py config.py
COPY database.py database.py
COPY logger.py logger.py
COPY models.py models.py
COPY schemas.py schemas.py
COPY main.py main.py

ENTRYPOINT ["python", "main.py"]