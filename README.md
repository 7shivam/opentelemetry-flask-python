"# opentelemetry-flask-python" 


export OTEL_TRACES_EXPORTER=jaeger_thrift
export OTEL_SERVICE_NAME=serviceA
export OTEL_EXPORTER_JAEGER_ENDPOINT=http://34.235.159.106:14268/api/traces
export OTEL_METRICS_EXPORTER=none


export OTEL_TRACES_EXPORTER=jaeger_thrift
export OTEL_SERVICE_NAME=serviceB
export OTEL_EXPORTER_JAEGER_ENDPOINT=http://34.235.159.106:14268/api/traces
export OTEL_METRICS_EXPORTER=none


opentelemetry-instrument python3 serviceA.py
