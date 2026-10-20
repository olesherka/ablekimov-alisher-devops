# base image with Python already installed
FROM python:3.12-slim

# all next commands work inside /app
WORKDIR /app

# copy the application and the student file into the image
COPY app/ /app/
COPY Ablekimov_Alisher_info.txt /app/

# check the code and create a user without root rights
RUN python -m py_compile app.py && useradd --create-home appuser
USER appuser

ENV APP_PORT=8080
EXPOSE 8080

CMD ["python", "-u", "app.py"]
