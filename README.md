# Data Lakehouse Project

## Introduction

This project is designed to construct a data lakehouse, enabling organizations to store, manage, and analyze large datasets in a cost-effective, secure, and scalable manner. The data lakehouse provides a centralized repository for all data, allowing users to easily access and query the data with a unified interface.

Key components include:

- **MinIO** for distributed object storage
- **Delta Lake** for ACID-compliant transactions
- **Apache Spark** for distributed computing and analytics
- **Presto** for fast SQL queries
- **Hive Metastore** for a unified data catalog
- **Apache Superset** for data visualization

This data lakehouse enables organizations to quickly and easily access and analyze valuable data, supporting better data-driven decisions.

## Description

**Warning**: This project is a work in progress and not yet ready for production use. Please use it at your own risk.

This platform integrates several specialized tools for data analytics, built on the following components:

- [Apache Spark](https://spark.apache.org/): A unified analytics engine for big data processing, with modules for streaming, SQL, machine learning, and graph processing.
- [Delta Lake](https://delta.io/): An open-source storage layer that brings ACID transactions to Apache Spark and big data workloads.
- [Apache Airflow](https://airflow.apache.org/): A platform to programmatically author, schedule, and monitor workflows.
- [MinIO](https://min.io/): A high-performance, distributed object storage system, 100% open source under the Apache V2 license.
- [Presto](https://prestodb.io/): A distributed SQL query engine designed for fast analytic queries against data of any size.
- [Hive Metastore](https://cwiki.apache.org/confluence/display/Hive/Hive+Metastore): A central repository of Hive metadata, storing metadata for Hive tables and partitions.
- [Apache Superset](https://superset.apache.org/): A modern data exploration and visualization platform.

### System Architecture

The system architecture is shown in the following diagram:
![lakehouse](./.images/Data-System-Architecture.png)

This architecture leverages stable technologies to build a scalable, reliable, and user-friendly data lakehouse platform. It supports storing, processing, and analyzing large amounts of data.

Despite using stable technologies, the platform is a work in progress. We are continuously improving the platform and adding new features. We welcome any suggestions or feedback to help us enhance the platform.

### Data Visualization

Visualize the data using Apache Superset.
![lakehouse](./images/sales_dashboard.png)

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- A basic understanding of the tools used in the platform.

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set up environment variables**:
   Create a `.env` file in the root directory and add the necessary environment variables, for example:

   ```env
   # MySQL
   MYSQL_HOST=mysql
   MYSQL_PORT=3306
   MYSQL_DATABASE=metastore_db
   MYSQL_ROOT_PASSWORD=admin
   MYSQL_USER=admin
   MYSQL_PASSWORD=admin

   # MinIO
   MINIO_ROOT_USER=minio
   MINIO_ROOT_PASSWORD=minio123
   MINIO_ACCESS_KEY=minio
   MINIO_SECRET_KEY=minio123

   # MinIO credentials
   AWS_ACCESS_KEY_ID=minio
   AWS_SECRET_ACCESS_KEY=minio123
   AWS_ACCESS_KEY=minio
   AWS_SECRET_KEY=minio123
   AWS_S3_ENDPOINT=http://minio:9000
   ```

3. **Build and run the services**:

   ```bash
   docker-compose up --build -d
   ```

4. **Access the services**:
   - **Superset**: [http://localhost:8088](http://localhost:8088)
   - **Presto**: [http://localhost:8080](http://localhost:8080)
   - **MinIO**: [http://localhost:9000](http://localhost:9000)
   - **Airflow**: [http://localhost:8080](http://localhost:8080)

## Usage

- **Apache Spark**: Use Spark for big data processing and analytics.
- **Delta Lake**: Ensure ACID transactions for your data.
- **Apache Airflow**: Schedule and monitor data workflows.
- **MinIO**: Store and retrieve data objects.
- **Presto**: Execute fast SQL queries on your data.
- **Hive Metastore**: Manage your metadata.
- **Apache Superset**: Visualize your data.
