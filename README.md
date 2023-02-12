# test
## test
### test


# first build
docker build . --tag f-app --no-cache
docker run -dit -p 5000:5000 --name flaskapp1 f-app

# rebuild 
docker container stop flaskapp1
docker rm flaskapp1
docker build . --tag f-app --no-cache
docker run -dit -p 5000:5000 --name flaskapp1 f-app
