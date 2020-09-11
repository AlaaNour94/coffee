#!/bin/sh
set -x

if [ "$1" = "flask" ];
then
    export FLASK_APP=main
    flask run --host 0.0.0.0 --port 9000

elif [ "$1" = "seed" ]
then
    export FLASK_APP=commands/seed
    flask seed_machines_data
    flask seed_pods_data
fi