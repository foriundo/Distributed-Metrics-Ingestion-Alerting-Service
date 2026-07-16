# Distributed-Metrics-Ingestion-Alerting-Service
A self-hosted observability backend that ingests high-cardinality time-series metrics through a Kafka-buffered pipeline, stores them in TimescaleDB, serves windowed aggregations over a REST query API, and runs a rule-based alerting engine with Redis-backed deduplication.
