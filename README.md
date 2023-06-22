"# opentelemetry-flask-python" 


export OTEL_TRACES_EXPORTER=jaeger_thrift
export OTEL_SERVICE_NAME=serviceA
export OTEL_EXPORTER_JAEGER_ENDPOINT=http://34.235.159.106:14268/api/traces
export OTEL_METRICS_EXPORTER=none


export OTEL_TRACES_EXPORTER=jaeger_thrift
export OTEL_SERVICE_NAME=serviceB
export OTEL_EXPORTER_JAEGER_ENDPOINT=http://34.235.159.106:14268/api/traces
export OTEL_METRICS_EXPORTER=none

OTEL_TRACES_EXPORTER=console,otlp
export OTEL_SERVICE_NAME=serviceA
export OTEL_EXPORTER_JAEGER_ENDPOINT=http://34.235.159.106:14268/api/traces
export OTEL_METRICS_EXPORTER=none

OTEL_TRACES_EXPORTER=console,otlp
export OTEL_SERVICE_NAME=serviceB
export OTEL_EXPORTER_JAEGER_ENDPOINT=http://34.235.159.106:14268/api/traces
export OTEL_METRICS_EXPORTER=none


opentelemetry-instrument python3 serviceA.py


OTEL_SERVICE_NAME=your-service-name \
OTEL_TRACES_EXPORTER=console,otlp \
OTEL_METRICS_EXPORTER=console \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317
opentelemetry-instrument \
    python myapp.py




    $ docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -p 5775:5775/udp \
  -p 6831:6831/udp \
  -p 6832:6832/udp \
  -p 5778:5778 \
  -p 16686:16686 \
  -p 14268:14268 \
  -p 14250:14250 \
  -p 9411:9411 \
  jaegertracing/all-in-one:latest

