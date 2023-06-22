From python:latest
ENV OTEL_TRACES_EXPORTER=jaeger_thrift
ENV OTEL_SERVICE_NAME=serviceB
ENV OTEL_EXPORTER_JAEGER_ENDPOINT=http://localhost:14268/api/traces
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["opentelemetry-instrument","python","-u","serviceB.py"]