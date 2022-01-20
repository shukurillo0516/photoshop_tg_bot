import os
import time
import platform
from datetime import datetime

from .models.model import append_to_db


path = '/media/shukurillo/8E10D62C10D61B53/my_folder/'
files_path = ['%s%s'%(path, x) for x in os.listdir(path)]


for file_p in files_path:
    if platform.system() == 'Windows':
        modTimesinceEpoc = os.path.getctime(file_p)
    else:
        statbuf = os.stat(file_p)
        modTimesinceEpoc = statbuf.st_mtime

    modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
    modificationTime = datetime.strptime(modificationTime, '%Y-%m-%d %H:%M:%S')

    append_to_db(file_p, modificationTime)