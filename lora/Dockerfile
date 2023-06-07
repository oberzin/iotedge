FROM ubuntu:bionic

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends libcurl4-openssl-dev python3 python3-pip 

RUN apt-get install -y python python-pip

#RUN pip install requests

RUN pip3 install requests

COPY . .

RUN useradd -ms /bin/bash lorauser
USER lorauser

EXPOSE 50005

CMD [ "python3", "-u", "./LoraReadServer.py" ]	
