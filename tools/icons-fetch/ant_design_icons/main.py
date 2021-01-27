import requests
import json
from os import walk, path, rename
import re
from shutil import copyfile
import zipfile
import io

DIST_DIR = "./dist"
ANT_ICONS_ROOT_DIR = "../res/ant-design-icons"
ANT_SVG_ROOT = ANT_ICONS_ROOT_DIR + "/packages/icons-svg/svg/"
REPOSITORY_ZIP_URL = "https://codeload.github.com/ant-design/ant-design-icons/zip/master"


def pre_warm():
    # download zip, unzip the repository
    print('downloading zip.. this might take a while')
    r = requests.get(REPOSITORY_ZIP_URL)
    filenamezip = r.headers.get('Content-Disposition').split('filename=')[-1]
    filename = filenamezip.split('.zip')[0]
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("../res")
    print(f'downloaded to ../res/{filename}')
    rename(f"../res/{filename}", "../res/ant-design-icons")
    print('res available under res/ant-design-icons')


def main():
    ...


if __name__ == "__main__":
    pre_warm()
    main()
