from .constants import (
    CNPJ_LENGTH,
    CPF_LENGTH,
)


def format_document(value: str) -> str:
    if not value:
        return ""
    value = value.strip()
    if len(value) == 11:
        return f"{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}"
    elif len(value) == 14:
        return f"{value[:2]}.{value[2:5]}.{value[5:8]}/{value[8:12]}-{value[12:]}"
    return value
