FROM python:3.6

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY fulhaus_app fulhaus_app
COPY run.py .

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=fulhaus_app:app

EXPOSE 5000
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# WORKDIR /fulhaus_app

# CMD [ "python3", "run.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# CMD ["flask", "run"]
