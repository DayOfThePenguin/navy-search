# Navsearch - Search Publicly Available Navy Instructions
## Tech stack
1. pdfs to text - [Apache Tika](https://tika.apache.org/)
2. raw text and metadata store - MongoDB
3. search indexing and backend - [MeiliSearch](https://docs.meilisearch.com/)

## Offline install
1. Create & activate new virtualenv
```shell
virtualenv env
source activate-env
```
2. Build and install a local wheel in your virtualenv 
```shell
make install
```
3. Run the tests
```shell
make test
```
4. Clone and build the MeiliSearch [repo](https://github.com/meilisearch/MeiliSearch)
```shell
git clone https://github.com/meilisearch/MeiliSearch.git
cd MeiliSearch
cargo run --release
```
5. Start the docker container with Apache Tika server and Mongodb (Tika to parse pdfs, Mongo to store raw parsed text and pdf metadata)
```shell
docker-compose up
```