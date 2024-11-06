FROM python:3.12.7-slim
COPY project2.python.entrypoints/bin.pex /bin/project2
# set PEX_MODULE=entrypoints.fizzbuzz to select module to execute
ENTRYPOINT ["python", "/bin/project2"]