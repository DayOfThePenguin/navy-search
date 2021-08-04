# Navsearch - Search (UNCLASS) Navy Instructions
## Tech stack
1. pdfs to text - [Apache Tika](https://tika.apache.org/)
2. raw text and metadata store - MongoDB
3. search indexing and backend - [MeiliSearch](https://docs.meilisearch.com/)

## Offline install 
```shell
sudo bin/elasticsearch-plugin install file:///path/to/plugin.zip
```

/usr/share/elasticsearch/bin/elasticsearch-plugin install file:///home/user/ingest-attachment-7.14.0.zip

[Ref](https://www.elastic.co/guide/en/elasticsearch/plugins/current/plugin-management-custom-url.html)