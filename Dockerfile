FROM python:3.10.4

WORKDIR /usr/code

COPY ./requirements.txt /usr/code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /usr/code/requirements.txt

COPY ./app /usr/code/app

ENV RELOAD=False

EXPOSE 8000

CMD ["python", "main.py"]