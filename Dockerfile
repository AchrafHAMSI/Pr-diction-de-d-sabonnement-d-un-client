FROM debian:latest
ADD . .
RUN apt-get update && apt-get install python3-pip -y && pip3 install fastapi && pip3 install -r /requirements.txt
EXPOSE 8000
CMD python3 api.py