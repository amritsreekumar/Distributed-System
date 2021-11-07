# # FROM python:3

# # RUN pip install sqlite-web

# from alpine:3.11

# RUN apk add --no-cache python3-dev \
#     && pip3 install --upgrade pip

# VOLUME /db
# # WORKDIR /db
# # COPY . /

# WORKDIR /app

# COPY . /app



# EXPOSE 5000

# RUN pip3 --no-cache-dir install -r requirements.txt
# # ENTRYPOINT ["sqlite_web", "--host=0.0.0.0", "--port=8080", "--no-browser"]
# ENTRYPOINT  ["python3"]

# CMD ["app.py"]
from alpine:3.11

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# VOLUME /weather

WORKDIR /app

COPY . /app



RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["app.py"]





