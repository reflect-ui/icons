from pathlib import Path
# from ..constants import icon_constants
# from organizer.models import model

VARIANT_MAP = {
    "solid": 'solid',
    "line": 'outlined',
    "monochrome": 'twotone',
    'thinline': 'thinline'
}


DIR_RAW_ORIGIN = "../../raw/unicons/svg"
DIR_RAW_METAFILES = "../../raw/unicons/json"
DIR_DIST_TARGER = "../../dist/tmp/unicons"


# the variants are the name to the target resource.
# in svg folder, the variant is a nested directory name
# in json folder, the variant is a file name
VARIANTS = ["line", "monochrome", "solid", "thinline"]


def mkdir_if_not_exists(path: Path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {path}")


def clear_dir(path: Path):
    if path.exists():
        for file in path.glob("*"):
            file.unlink()
        print(f"Cleared directory: {path}")


def flat_oraganize_all_files():
    # Merge the raw icons svg folder (by variant names), merge into one directory with variant name as suffix
    # e.g. /raw/unicons/svg/line/0-plus.svg -> dist/tmp/unicons/0-plus-outlined.svg

    # init the target dir relative to this file
    dist = Path(__file__).parent.joinpath(DIR_DIST_TARGER)
    mkdir_if_not_exists(dist)
    # clear_dir(dist)

    for variant in VARIANTS:
        universal_variant_name = VARIANT_MAP[variant]
        variant_dir = Path(__file__).parent.joinpath(
            f"{DIR_RAW_ORIGIN}/{variant}")
        for svg_file in variant_dir.glob("*.svg"):
            svg_file_name = svg_file.name
            new_name = svg_file_name.replace(
                ".svg", f"-{universal_variant_name}.svg")
            svg_file_target = Path(__file__).parent.joinpath(
                f"{DIR_DIST_TARGER}/{new_name}")

            # copy file to target with new name
            svg_file_target.write_text(svg_file.read_text())

    pass


def sanitize_svg(path):
    # remove the attribute "data-layer"
    # remove the class prefix with "uim-" (class="uim-primary" -> class="primary")
    pass


if __name__ == '__main__':
    flat_oraganize_all_files()
