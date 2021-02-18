#FROM python:3.7-alpine
FROM python:3.7
RUN apt-get update && \
    apt-cache search mysql-client && \
    apt install -y default-mysql-client
RUN mkdir /codigo
COPY requirements.txt /codigo/
WORKDIR /codigo
RUN pip install -r requirements.txt
RUN pip install parameterized
COPY run.sh /codigo/
RUN chmod ugo+x /codigo/run.sh
COPY *.py /codigo/
CMD [ "python3", "ejemplo4.py" ]
