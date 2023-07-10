FROM python:3.8.5-slim as base

MAINTAINER Yuval Yaari
LABEL version="0.1"

RUN pip3 install flask==2.1.2

WORKDIR /src/
COPY api.py .

FROM base as test
COPY api_test.py .
RUN pip3 install pytest werkzeug=='2.1.2'
CMD ["python3", "-m", "pytest", "-v"]

FROM base as production
EXPOSE 5000
ENTRYPOINT ["python3", "api.py"]