FROM python:3.7
RUN apt-get update && \
#    /usr/local/bin/python -m pip install --upgrade pip &&\
    apt-cache search mysql-client && \
    apt install -y default-mysql-client && \
    apt install nano
RUN mkdir /codigo
COPY requirements.txt /codigo/
WORKDIR /codigo
RUN pip install -r requirements.txt
COPY wait-for-it.sh /codigo/
RUN chmod +x /codigo/wait-for-it.sh
COPY *.py /codigo/
CMD ["./wait-for-it.sh", "-t", "0", "-h", "mysql", "-p", "3306", "--", "python3", "temp.py"]

