  523  cd ../exercice-2-weather-api/
  524  git checkout -b tp/Lucas-HENNEBELLE
  525  touch .dockerignore
  526  touch Dockerfile
  532  docker build -t shogaro/weather-api:1.0.0
  533  docker build -t shogaro/weather-api:1.0.0 .
  534  docker run -d -p 10:3000 shogaro/weather-api:1.0.0 
  535  docker push shogaro/weather-api:1.0.0
  537  docker tag shogaro/weather-api:1.0.0 shogaro/weather-api:latest && docker push shogaro/weather-api:latest
  539  history > COMMANDS.md
