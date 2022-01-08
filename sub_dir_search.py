# sub_dir_search.py

import os

def search(dirname):
    try:
        filenames = os.listdir(dirname) # 해당 디렉터리에 있는 파일들의 리스트 
        for filename in filenames: 
            full_filename = os.path.join(dirname, filename) # 디렉터리와 파일이름을 이어준다.
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splittext(full_filename)[-1] # 파일이름에서 확장자만 추출
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("c:\")

'''
import os

for (path, dir, files) in os.walk("c:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))
'''
