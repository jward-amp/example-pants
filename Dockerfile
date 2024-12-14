FROM python:3.12-slim
WORKDIR /app
COPY 3rdparty/python/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY common common
COPY project1 project1
COPY project2 project2

RUN pip install common/python && \
    pip install project1/python && \
    pip install project2/python

ENTRYPOINT ["python"]