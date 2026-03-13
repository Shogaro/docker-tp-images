  502  git clone git@github.com:Shogaro/docker-tp-images.git
  503  cd docker-tp-images/
  504  cd exercice-1-flask/
  506  docker build -t hello-flask:1.0.0
  508  docker build -t hello-flask:1.0.0 .
  509  docker tag hello-flask:1.0.0 hello-flask:latest
  510  docker run -d hello-flask:1.0.0 
  514  docker run -d hello-flask:1.0.0 5000:5000
  515  docker run -d hello-flask:1.0.0 -p 5000:5000
  516  docker run -d -p 5000:5000  hello-flask:1.0.0
  519  docker images | grep hello-flask
  521  history > COMMANDS.md
