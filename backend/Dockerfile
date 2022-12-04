FROM tiangolo/uvicorn-gunicorn:python3.11-slim


ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1

# upgrade pip
RUN pip install --upgrade pip

ENV APP_HOME /usr/src/app

WORKDIR /$APP_HOME

COPY . $APP_HOME/

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

