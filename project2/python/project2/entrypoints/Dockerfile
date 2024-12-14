FROM python:3.12.7-slim
COPY project2.python.project2.entrypoints/bin.pex /bin/project2
# set PEX_MODULE=entrypoints.fizzbuzz to select module to execute
ENTRYPOINT ["python", "/bin/project2"]