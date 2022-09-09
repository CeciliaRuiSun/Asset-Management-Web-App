#!/bin/bash

  curl -X POST \
   -H "Authorization: JWT ${TOKEN}" \
   -H "Content-Type: application/json" \
   "http://127.0.0.1:5000/item?name=T11"
   #-d '{ "price": 100 }' \
