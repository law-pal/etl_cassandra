# Project 2: Data Modeling with Apache Cassandra

This project creates an Apache Cassandra database for a music app, *Sparkify*. I created an ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file **event_datafile_new.csv** which is used to populate the denormalized Cassandra tables to model and insert data into the NoSQL database.

The 3 tables in the model are named after the song play query they are created to solve:

1. **` songs_by_session_and_item`** includes artist, song title and song length information for a given `sessionId` and `itemInSessionId`.

2. **`user_by_name_and_session`** includes artist, song and user for a given `userId` and `sessionId`.

3. **`user_by_firstname_and_lastname`** includes user names for a given song.

The queries are returned as pandas dataframes to facilitate further data manipulation.

<br>

> **Note:** This project can be run in a docker container.

## Run in a Docker container

With docker installed, pull the latest Apache Cassandra image and run the container as follows:

```{bash}
docker pull cassandra
docker run --name cassandra-container -p 9042:9042 -d cassandra:latest
```

Pulling the image will allow you to create the data model and etl pipeline, without altering the original connection code connecting to localhost port 9042.

```{python}
from cassandra.cluster import Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
```

To stop and remove the container after the exercise

```{bash}
docker stop cassandra-container
docker rm cassandra-container
```