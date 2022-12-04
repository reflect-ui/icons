from setuptools.package_index import safe_name


def make_icon_full_name(icon_name, icon_variant, token='_'):
    return f"{icon_name}{token}{icon_variant}" if icon_variant != "" else icon_name


def make_icon_full_name_with_size(icon_name, icon_variant, size):
    return f'{make_icon_full_name(icon_name, icon_variant)}_{size}'
