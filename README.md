# Distributed-Metrics-Ingestion-Alerting-Service
A self-hosted observability backend that ingests high-cardinality time-series metrics through a Kafka-buffered pipeline, stores them in TimescaleDB, serves windowed aggregations over a REST query API, and runs a rule-based alerting engine with Redis-backed deduplication.

# Tech Stack
- Python/ FastAPI
- Kafka
- TimescaleDB
- Redis
- Docker

# To run it
'''
uv run uvicorn metrics_services.main:app --reload
'''