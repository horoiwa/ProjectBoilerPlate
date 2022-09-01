#!/bin/bash
set -eu

cmd=$1

project_tag="$(basename $(pwd))_$(whoami)"
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

# bind-mount先のディレクトリが存在しない場合は事前作成しておかないと所有権がrootになる
if [ ! -d ./log ]; then
  mkdir ./log
fi

# up: コンテナimageのbuildとup
if [ $cmd = "up" ]; then
  echo "Build image and up compose"
  sudo docker-compose -p $project_tag build  \
       --build-arg UID=$uid --build-arg GID=$gid --build-arg GROUPNAME=$gname
  sudo docker-compose -p $project_tag up -d
  echo "Finished"

# login: コンテナへBashでログイン
elif [ $cmd = "login" ]; then
  # コンテナがupしているかチェック
  if [ "`sudo docker-compose -p $project_tag ps | grep 'Up'`" ]; then
    echo "Login to container"
    sudo docker-compose -p $project_tag exec pyenv bash
  else
    echo "Error: コンテナが起動していません, './cmd.sh up' を実行してください"
  fi
elif [ $cmd = "production" ]; then
  echo "Product run"
  sudo docker-compose -p $production_tag build  \
       --build-arg UID=$uid --build-arg GID=$gid --build-arg GROUPNAME=$gname
  sudo docker-compose -p $production_tag -f docker-compose.yml -f production.yml up -d
  sudo docker-compose -p $production_tag exec pyenv bash

else
  echo "無効なコマンド: ${cmd}"
fi
