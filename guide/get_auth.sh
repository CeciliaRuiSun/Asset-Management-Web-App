#!/bin/bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"username": "user1", "password": "abcxyz"}' \
    http://127.0.0.1:5000/auth

