# Contents Service Management (CSM)

## Development environment

- python 3.6
- docker 19.03.8
- docker-compose 1.17.1
- influxdb 1.17.10

## nginx + flask + influxdb
- flask : flask + uwsgi
- nginx : uwsgi_pass (proxy pass)
- influxdb

## How to install
#### 1. install docker (for Linux) && docker-compose

1-1. docker 

```sh
curl -fsSL get.docker.com -o get-docker.sh
sh get-docker.sh
```

after running the command, you can confirm which it works using the command below

```sh
$ docker --version
Docker version 19.03.8, build 1234567890
```

1-2. docker-compose

```sh
$ sudo curl -L https://github.com/docker/compose/releases/download/1.17.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
```

after running the command, you can confirm which it works using the command below

```sh
$ docker-compose --version
docker-compose version 1.17.1, build 6d101fb
```


#### 2. clone this folder

   ```sh
$ git clone 
   ```

#### 3. run the **docker-compose.yml** in the folder

   ```sh
$ cd keti_decenter
$ docker-compose up
   ```

   After running this command, you can see a list of 2 running containers on docker

   ```sh
$ docker ps
   
   CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
   f8f244427369        nginx:test          "nginx -g 'daemon of…"   18 seconds ago      Up 17 seconds       0.0.0.0:80->80/tcp       nginx
   7dd1b4ec51f7        flask:test          "/bin/sh -c 'uwsgi u…"   19 seconds ago      Up 18 seconds       0.0.0.0:5000->5000/tcp   flask
   
   ```

#### 4. run a random dump data generator named 'test.py' (for test)

   open a new terminal

```sh
$ python test.py
```

#### 5. open the url 'http://localhost/'

   you can see the main page of SCM



## Images



<img src=".\images\ui_final_2.png" alt="ui_final_2" style="zoom:20%;" />