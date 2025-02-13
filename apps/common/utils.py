from nanoid import generate


def id_with_prefix(prefix: str) -> str:
    return f'{prefix}_{generate()}'


def generate_id_with_prefix(prefix: str, _size: int):
    return f'{prefix}_{generate(size=_size)}'
