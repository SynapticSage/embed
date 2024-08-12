#!/usr/bin/env sh

if [ -f "$(which embed)" ]; then
  embed_path=$(which embed)
elif [ -f "$(which embed.sh)" ]
then
  embed_path=$(which embed.sh)
else
  echo "embed.sh: command not found"
  exit 1
fi
embed_path=$(readlink -f "$embed_path")
path=$(dirname "${embed_path}")

module="${path}/embedkit"

. "${path}/env/bin/activate" && python "${module}/embed.py" "$@"
