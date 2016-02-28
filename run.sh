#!/bin/bash

trap killgroup SIGINT

killgroup(){
  echo killing...
  kill 0
}

source .env/bin/activate
python app.py &
ember server --proxy http://localhost:5000 &
wait
