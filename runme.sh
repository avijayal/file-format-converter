source /home/vijaya/file-format-converter/ffc-venv/bin/activate
export SRC_BASE_DIR=/home/vijaya/file-format-converter/data/retail_db
export TGT_BASE_DIR=/home/vijaya/file-format-converter/data/retail_demo
export LOG_FILE_PATH=/home/vijaya/file-format-converter/logs/ffc-log
export SCHEMAS_FILE_PATH=/home/vijaya/file-format-converter/data/retail_db/schemas.json


rm -rf $TGT_BASE_DIR
mkdir -p /home/vijaya/file-format-converter/logs
ffc
deactivate