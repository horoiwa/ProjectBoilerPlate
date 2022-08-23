#!/bin/bash

cmd=$1

project_tag="$(basename $(pwd))_$(whoami)"
production_tag="$(basename $(pwd))_prod"

uid=$(id -u)
gid=$(id -g)
gname=$(id -g -n)
uname=$(id -u -n)

# プロジェクト直下に移動
cd $(dirname $0)

# bindmount先のディレクトリが存在しない場合は作成しておかないと所有権がrootになる
if [ ! -d ./log ]; then
  mkdir ./log
fi

if [ $cmd = "up" ]; then
  echo "Build image and up compose"
  sudo docker-compose -p $project_tag build  \
       --build-arg UID=$uid --build-arg GID=$gid --build-arg GROUPNAME=$gname
  sudo docker-compose -p $project_tag up -d
  echo "Finished"

elif [ $cmd = "login" ]; then
  echo "Login to container"
  sudo docker-compose -p $project_tag exec pyenv bash

elif [ $cmd = "production" ]; then
  echo "Product run"
  sudo docker-compose -p $production_tag build  \
       --build-arg UID=$uid --build-arg GID=$gid --build-arg GROUPNAME=$gname
  sudo docker-compose -p $production_tag -f docker-compose.yml -f production.yml up -d
  sudo docker-compose -p $production_tag exec pyenv bash

else
  echo "無効なコマンド: ${cmd}"
fi
