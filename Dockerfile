FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "main.py" ]

#FROM python:3.11-slim-bullseye as compile-image
#RUN python -m venv /opt/venv
#ENV PATH="/opt/venv/bin:$PATH"
#COPY requirements.txt .
#RUN apt update
#RUN apt-get -y install pkg-config
##RUN export MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
##RUN export MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu"
##RUN pip install mysqlclient
##RUN pip install mariadb
#
#RUN pip install --no-cache-dir --upgrade pip \
# && pip install --no-cache-dir -r requirements.txt
#
#FROM python:3.9-slim-bullseye
#COPY --from=compile-image /opt/venv /opt/venv
#ENV PATH="/opt/venv/bin:$PATH"
#WORKDIR /app
#COPY . /app
#CMD ["python", "-m", "pythonback"]