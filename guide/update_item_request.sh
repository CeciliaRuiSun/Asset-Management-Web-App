#!/bin/bash

  curl -X PUT \
   -H "Authorization: JWT ${TOKEN}" \
   -H "Content-Type: application/json" \
   -d "{ 'quantity': 100 }" \
   "http://127.0.0.1:5000/item/T5"
