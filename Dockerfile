FROM python:3.9-slim
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main/main.py main.py
COPY main/sprites/ sprites/
RUN apt-get update
RUN apt-get install -y libxrender-dev libx11-6 libxext-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*
CMD ["python", "main.py"]