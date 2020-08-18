FROM python:3.8.5-alpine

WORKDIR /opt/app/therecord/
COPY . /opt/app
RUN python3 -m venv env
RUN source env/bin/activate
RUN pip install django
RUN pip install djangorestframework
RUN pip install requests
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
