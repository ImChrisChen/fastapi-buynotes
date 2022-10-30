import os
from datetime import datetime

from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    tags=['文件上传'],
    prefix='/upload'
)


def get_filepath(f):
    timedate = datetime.now().strftime('%Y%m%d_%H%M_%s')
    [filename, suffix] = os.path.splitext(f.filename)
    filename_fmt = f'{filename}_{timedate}{suffix}'
    filepath = os.path.join(os.path.abspath('.'), 'static/upload', filename_fmt)
    print(filepath)
    return filepath


@router.post('/')
async def upload_file(f: UploadFile = File(...)):
    if f.filename == '':
        return {
            'code': -1,
            'msg': 'please choice file upload!'
        }
        pass
    file_content = f.file.read()
    print(file_content)
    filepath = get_filepath(f)

    try:
        with open(filepath, 'w') as new_file:
            print(new_file)
            new_file.write(str(file_content))
            return {
                'code': 0,
                'msg': 'ok'
            }
    except BaseException as e:
        return {
            'code': -1,
            'error': e,
            'msg': 'fail',
        }

