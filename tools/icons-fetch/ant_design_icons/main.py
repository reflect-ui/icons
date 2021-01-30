import os

import requests
import json
from os import walk, path, rename
import re
from shutil import copyfile
import zipfile
import io

import constants.icon_constants
import models.model
from utils.icon_names import make_icon_full_name

DIST_DIR = "./dist"
ANT_ICONS_ROOT_DIR = "../res/ant-design-icons"
ANT_SVG_ROOT = ANT_ICONS_ROOT_DIR + "/packages/icons-svg/svg/"
REPOSITORY_ZIP_URL = "https://codeload.github.com/ant-design/ant-design-icons/zip/master"


def should_pre_warm():
    # if directory already exists, it means the zip file is downloaded on previous load.
    return not path.isdir(ANT_ICONS_ROOT_DIR)

def pre_warm():
    # download zip, unzip the repository
    print('downloading zip.. this might take a while')
    r = requests.get(REPOSITORY_ZIP_URL)
    filenamezip = r.headers.get('Content-Disposition').split('filename=')[-1]
    filename = filenamezip.split('.zip')[0]
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("../res")
    print(f'downloaded to ../res/{filename}')
    rename(f"../res/{filename}", ANT_ICONS_ROOT_DIR)
    print('res available under res/ant-design-icons')


def prepare_dump():
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR)


# on ant-design/ant-design-icons - packages/icons-svg/svg/
ANTD_SVG_ICON_DIR_VARIANT_NAMES = ["filled", "outlined", "twotone"]

ANTD_SVG_ICON_DIR_VARIANT_NAME_MAP = {
    "filled": constants.icon_constants.ICON_VARIANT_DEFAULT,
    "outlined": constants.icon_constants.ICON_VARIANT_OUTLINED,
    "twotone":  constants.icon_constants.ICON_VARIANT_TWOTONE
}


def icon_name_from_file_name(file_name: str):
    # `add.svg` to `add`
    return file_name.split('.svg')[0]


def main():
    prepare_dump()
    config = {}
    for variant_dir in ANTD_SVG_ICON_DIR_VARIANT_NAMES:
        svg_dir = path.join(ANT_SVG_ROOT, variant_dir)
        variant_name = ANTD_SVG_ICON_DIR_VARIANT_NAME_MAP[variant_dir]
        print(variant_name, svg_dir)
        for (dirpath, dirnames, filenames) in walk(svg_dir):
            for file_name in filenames:
                svg_path = path.join(dirpath, file_name)
                icon_name = icon_name_from_file_name(file_name)
                icon_full_name = make_icon_full_name(icon_name, variant_name, token='-')
                single_icon_config = models.model.SingleIconConfig(
                        default_size= constants.icon_constants.ICON_DEFAULT_SIZE,
                        variant=variant_name,
                        family= icon_name,
                        host=constants.icon_constants.ICON_ORIGIN_HOST_ANTD
                    )
                single_config = single_icon_config.to_object()
                config[icon_full_name] = single_config

                out = f"{DIST_DIR}/{icon_full_name}.svg"
                copyfile(svg_path, out)
                print(single_config)

    with open(f'{DIST_DIR}/config.json', 'w') as file:
        json.dump(config, file, indent=2)

    print(config)

if __name__ == "__main__":
    if should_pre_warm():
        pre_warm()
    main()
