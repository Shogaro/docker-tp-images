  541  cd ../exercice-3-stats-api/
  542  touch Dockerfile
  543  touch .dockerignore
  544  docker build -t shogaro/stats-api:1.0.0 .
  545  docker run -dp 8080:8080 shogaro/stats-api:1.0.0 
  546  docker login
  547  docker push shogaro/stats-api:1.0.0 
  548  docker build -t shogaro/stats-api:2.0.0 .
  551  docker run -dp 8080:8080 shogaro/stats-api:2.0.0
  552  docker tag shogaro/stats-api:2.0.0 shogaro/stats-api:latest
  553  docker images | grep shogaro/stats-api
  554  docker push shogaro/stats-api:2.0.0 
  555  docker push shogaro/stats-api:latest
  556  history > COMMANDS.md
