#!/bin/bash
set -eu

cmd=$1

tag="$(basename $(pwd))_$(whoami)"
production_tag="$(basename $(pwd))_prod"

uid=$(id -u)
gid=$(id -g)
gname=$(id -g -n)
uname=$(id -u -n)

# プロジェクト直下に移動
cd $(dirname $0)

# root実行は想定していない
if [[ $uid = "0" ]]; then
  echo "Error: Please run as non-root user"
  echo "Exit"
  exit 1
fi

# up: コンテナimageのbuildとup
if [ $cmd = "up" ]; then
  echo "Build image and up compose"
  sudo docker-compose -p $tag build  \
       --build-arg UID=$uid --build-arg GID=$gid --build-arg GROUPNAME=$gname
  sudo docker-compose -p $tag up -d
  echo "Finished"

# login: コンテナへBashでログイン
elif [ $cmd = "login" ]; then
  # コンテナがupしているかチェック
  if [ "`sudo docker-compose -p $tag ps | grep 'Up'`" ]; then
    echo "Login to container"
    sudo docker-compose -p $tag exec pyenv bash
  else
    echo "Error: コンテナが起動していません, './cmd.sh up' を実行してください"
  fi

elif [ $cmd = "production" ]; then
  echo "Product run"
  sudo docker-compose -p $production_tag build  \
       --build-arg UID=$uid --build-arg GID=$gid --build-arg GROUPNAME=$gname
  sudo docker-compose -p $production_tag -f docker-compose.yml -f production.yml up -d

else
  echo "無効なコマンド: ${cmd}"
fi
