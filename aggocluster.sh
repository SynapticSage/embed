#!/usr/bin/env sh

if [ -f "$(which aggocluster)" ]; then
  embed_path=$(which embed)
elif [ -f "$(which aggocluster.sh)" ]
then
  embed_path=$(which aggocluster.sh)
else
  echo "aggocluster.sh: command not found"
  exit 1
fi
embed_path=$(readlink -f "$embed_path")
path=$(dirname "${embed_path}")

module="${path}/embedkit"

. "${path}/env/bin/activate" && python "${module}/agglomerative_cluster.py" "$@"
