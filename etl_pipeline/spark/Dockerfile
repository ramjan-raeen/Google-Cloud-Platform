FROM apache/spark:3.5.6

USER root

ENV SPARK_HOME=/opt/spark
ENV PATH="${SPARK_HOME}/bin:${PATH}"

# Create application directory
RUN mkdir -p /opt/spark-apps

WORKDIR /opt/spark-apps

# Copy application
COPY app/ /opt/spark-apps/

USER spark