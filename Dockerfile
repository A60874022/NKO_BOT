FROM python:3.10-slim-buster


WORKDIR app/


COPY . .

# Устанавливаем все необходимые пакеты python из requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python", "nko_bot.py"] 