# Docker

![docker_sheme](images/docker_container.png)

![docker_cycle](images/cycle.png)

![ports](images/ports.png)

![volumes](images/volumes.png)

![volume_types](images/volume_types.png)

![networks](images/networks.png)

![network_types](images/network_types.png)

![dockerfile](images/dockerfile.png)

![docker_compose](images/docker_compose.png)

![docker_compose_2](images/docker_compose_2.png)


### docker

* docker --version
* docker pull "image"
* docker run -d --rm -it --name "container" -p 80:80 -p 433:80 -e NAME=Vlad 
-v app:/var/www/html "image:version" --net my-network "cmd in container"
* docker exec -it "container" /bin/bash or "immediately in workdir"
* docker system prune -a --volumes — remove all stopped or useless images & containers

<br>

* docker ps -a
* docker rm -f "container"

<br>

* docker images
* docker rmi "image"

<br>

* docker kill "container"
* docker pause / unpause "container"
* docker stop / start / restart "container"

<br>

* docker logs -f "container" — updated
* docker stats "container" — CPU | Memory
* docker inspect "container"

<br>

* docker volume ls
* docker volume rm "volume"
* docker volume prune
* docker volume create "volume_name"

<br>

* docker network ls
* docker network rm "network"
* docker network inspect "network"
* docker network connect / disconnect "network" "container"
* docker network create "network_name" -d bridge 
--subnet "192.108.10/24" --gateway 192.108.10.1 --ip-range
(***--net*** for containers)

<br>

* docker tag <image> <new_tag>
* docker build . -t my_image:v01


### docker compose

* docker compose build .
* docker compose up -d --build 
* docker compose down -v
* docker compose logs -f
* docker compose stop / start / restart


### system

* useradd -m -s /bin/bash "username"
* usermod -aG docker "username"

<br>

* sudo su -
* sudo -i -u emurze
* chmod +x manage.py

<br>

* service docker status
* service docker stop / start / restart

<br>

* env
* ps xa
* netstat --tuplen
* ip a | ifconfig
* curl -Li "ip | domain"
* gnome-system-monitor
