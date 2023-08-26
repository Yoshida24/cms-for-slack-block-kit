#!/bin/bash
set -a && source ./.env && set +a
python ./src/demo/gspread_write.py