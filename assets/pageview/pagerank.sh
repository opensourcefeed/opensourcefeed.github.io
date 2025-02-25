#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS=credentials.json
source .env/bin/activate
python3 fetch4.py