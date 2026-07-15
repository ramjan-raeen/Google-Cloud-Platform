
FROM debian:bookworm-slim AS builder

ARG DEBEZIUM_VERSION=2.7.3.Final

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget ca-certificates && \
    wget -q https://repo1.maven.org/maven2/io/debezium/debezium-connector-mysql/${DEBEZIUM_VERSION}/debezium-connector-mysql-${DEBEZIUM_VERSION}-plugin.tar.gz -O /tmp/debezium.tar.gz && \
    mkdir -p /plugins/debezium-connector-mysql && \
    tar -xzf /tmp/debezium.tar.gz -C /plugins/debezium-connector-mysql --strip-components=1 && \
    rm -f /tmp/debezium.tar.gz

# Stage 2: the actual runtime image — no package manager needed here at all
FROM apache/kafka:3.9.1

RUN mkdir -p /opt/kafka/plugins
COPY --from=builder /plugins /opt/kafka/plugins

WORKDIR /opt/kafka

