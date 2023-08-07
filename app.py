# def hw():
#     print('hello world')
#     return
# print(__name__)
import json
import uuid
import os
import glob
import pandas as pd
import logging


# Avoiding hard coding using environment variables
# def get_columns(ds):
#     schemas_file_path = os.environ.setdefault('SCHEMAS_FILE_PATH','data/retail_db/schemas.json')
#     with open(schemas_file_path)as fp:
#         schemas=json.load(fp)
#     try:
#         file=schemas.get(ds)
#         if not file:
#             raise KeyError
#         cols=sorted(file,key=lambda s:s['column_position'])
#         columns=[col['column_name']for col in cols]
#         return columns
#     except KeyError:
#         print(f'schema not found for {ds}')
#         return
# def main():
#     src_base_dir = os.environ['SRC_BASE_DIR']
#     tgt_base_dir = os.environ['TGT_BASE_DIR']   
#     for path in glob.glob(f'{src_base_dir}/*'):
#         if os.path.isdir(path):
#             ds=os.path.split(path)[1]
#             for file in glob.glob(f'{path}/*'):
#                 df=pd.read_csv(file,names=get_columns(ds))
#                 os.makedirs(f'{tgt_base_dir}/{ds}',exist_ok=True)
#                 df.to_json(
#                     f'{tgt_base_dir}/{ds}/part-{str(uuid.uuid1())}.json',
#                     orient='records',
#                     lines=True
#                 )
#                 print(f'no.of records processed for {os.path.split(file)[1]} in {ds} is {df.shape[0]}')


# if __name__=='__main__':
#     main()
    
# modularizing using environment variables
def get_columns(ds):
    schemas_file_path = os.environ.setdefault('SCHEMAS_FILE_PATH','data/retail_db/schemas.json')
    with open(schemas_file_path)as fp:
        schemas=json.load(fp)
    try:
        file=schemas.get(ds)
        if not file:
            raise KeyError
        cols=sorted(file,key=lambda s:s['column_position'])
        columns=[col['column_name']for col in cols]
        return columns
    except KeyError as ke:
        logging.error(f'schema not found for {ds}')
        raise
    
def proces_file(src_base_dir,ds,tgt_base_dir):
    for file in glob.glob(f'{src_base_dir}/{ds}/part*'):
        try:
            df=pd.read_csv(file,names=get_columns(ds))
            os.makedirs(f'{tgt_base_dir}/{ds}',exist_ok=True)
            df.to_json(
                f'{tgt_base_dir}/{ds}/part-{str(uuid.uuid1())}.json',
                orient='records',
                lines=True
            )
            logging.info(f'no.of records processed for {os.path.split(file)[1]} in {ds} is {df.shape[0]}')
        except KeyError:
            raise

def main():
    logging.basicConfig(
    filename='logs/ffc.log',
    level=logging.INFO,
    format='%(levelname)s %(asctime)s %(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %p'
    )
    src_base_dir = os.environ['SRC_BASE_DIR']
    tgt_base_dir = os.environ['TGT_BASE_DIR']
    datasets = os.environ.get('DATASETS')
    logging.info('File format conversion:started')
    if not datasets:   
        for path in glob.glob(f'{src_base_dir}/*'):
            if os.path.isdir(path):
                proces_file(src_base_dir,os.path.split(path)[1],tgt_base_dir)
    else:
        dirs=datasets.split(',')
        for ds in dirs:
            try:
                proces_file(src_base_dir,ds,tgt_base_dir)
            except Exception as e:
                logging.error(f'file format conversion for {ds} is not successful')
    logging.info('File format conversion:successful')
 

if __name__=='__main__':
    main()