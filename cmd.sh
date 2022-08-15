#!/bin/bash

cmd=$1

uid=$(id -u)
gid=$(id -g)
gname=$(id -g -n)
uname=$(id -u -n)

# プロジェクト直下に移動
cd $(dirname $0)

# ./log/が存在しない場合は作成
if [ ! -d ./log ]; then
  mkdir ./log
fi

if [ $cmd = "up" ]; then
  echo "Build image and up compose"
  sudo docker-compose build  \
       --build-arg UID=$uid --build-arg GID=$gid --build-arg GROUPNAME=$gname
  sudo docker-compose up -d
  echo "Finished"

elif [ $cmd = "login" ]; then
  echo "Login to container"
  sudo docker-compose exec pyenv bash

elif [ $cmd = "product" ]; then
  echo "Start product run"

else
  echo "無効なコマンド: ${cmd}"
fi
