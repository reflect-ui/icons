import json
from os import walk, path, rename
import re
from shutil import copyfile
import requests
import zipfile
import io

DIST_DIR = "./dist"
MATERIAL_ICONS_ROOT_DIR = "../../res/material-design-icons"
MATERIAL_ICONS_SVG_DIR = MATERIAL_ICONS_ROOT_DIR + "/src"
REPOSITORY_ZIP_URL = "https://codeload.github.com/google/material-design-icons/zip/master"


def pre_warm():
    # download zip, unzip the repository
    print('downloading zip.. this might take a while')
    r = requests.get(REPOSITORY_ZIP_URL)
    filenamezip = r.headers.get('Content-Disposition').split('filename=')[-1]
    filename = filenamezip.split('.zip')[0]
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("../res")
    print(f'downloaded to res/{filename}')
    rename(f"res/{filename}", MATERIAL_ICONS_ROOT_DIR)
    print('res available under res/material-design-icons')


SIZE_VARIANT_NAME_MAP = {
    "materialiconsoutlined": "outlined",
    "materialiconsround": "round",
    "materialiconssharp": "sharp",
    "materialicons": "",
    "materialiconstwotone": "twotone",
}

SIZE_VARIANT_FLUTTER_NAME_MAP = {
    "outlined": "outlined",
    "round": "round",
    "sharp": "sharp",
    "": "",
    "twotone": "twotone"
}


def make_icon_full_name(icon_name, icon_variant):
    return f"{icon_name}_{icon_variant}" if icon_variant != "" else icon_name


def make_icon_full_name_with_size(icon_name, icon_variant, size):
    return f'{make_icon_full_name(icon_name, icon_variant)}_{size}'


def get_icon_info_from_path(svg_path):
    splits = svg_path.split('/')
    icon_name = splits[-3]
    icon_variant = SIZE_VARIANT_FLUTTER_NAME_MAP[SIZE_VARIANT_NAME_MAP[splits[-2]]]
    size = re.search(r'(.*?)px\.svg', splits[-1]).group(1)
    return icon_name, icon_variant, size


def main():
    config = {}

    # Get the list of all files in directory tree at given path
    svg_paths = list()
    for (dirpath, dirnames, filenames) in walk(MATERIAL_ICONS_SVG_DIR):
        svg_paths += [path.join(dirpath, file) for file in filenames]

    for svg_path in svg_paths:
        icon_name, icon_variant, size = get_icon_info_from_path(svg_path)
        icon_full_name = make_icon_full_name(icon_name, icon_variant)
        icon_full_name_with_size = make_icon_full_name_with_size(
            icon_name, icon_variant, size)
        print(icon_name, icon_variant, size)
        config[icon_full_name] = {
            "default_size": size,
            "variant": "default" if icon_variant == "" else icon_variant,
            "family": icon_name,
            "host": "material"
        }

        out = f"{DIST_DIR}/{icon_full_name_with_size}.svg"
        copyfile(svg_path, out)
    print(config)
    with open(f'{DIST_DIR}/config.json', 'w') as file:
        json.dump(config, file, indent=2)

    with open(f'{DIST_DIR}/full-packed.txt', 'w') as file:
        for svg_path in svg_paths:
            icon_name, icon_variant, size = get_icon_info_from_path(svg_path)
            with open(svg_path, 'r') as svg_file:
                content = svg_file.read()
                line = f'{make_icon_full_name_with_size(icon_name, icon_variant, size)}={content}\n'
                file.writelines(line)


if __name__ == '__main__':
    pre_warm()
    # main()
#
# def main():
#     # file structure is like
#     # -src
#     #     - category_name
#     #       - icon_name
#     #         - 24px.svg
#
#     svg_maps = {}
#     a = [x[0] for x in walk(MATERIAL_ICONS_SVG_DIR)]
#     print(a)
#
#
#     categories = [f for f in listdir(MATERIAL_ICONS_SVG_DIR) if isdir(join(MATERIAL_ICONS_SVG_DIR, f))]
#     print(categories)
#     for category in categories:
#         icon_dirs = [c for c in listdir(category) if isdir(category, c)]
#         print(icon_dirs)
#         for icon_name_dir in icon_dirs:
#             # looping through the directory, but it will have only 24px.svg under it.
#             svgs = [f for f in listdir(
#                 icon_name_dir) if isfile(join(icon_name_dir, f))]
#
#             for svg_path in svgs:
#                 icon_name = icon_name_dir.split('/')[-1]
#                 svg_maps[icon_name] = svg_path
#
#     print(svg_maps)
#
