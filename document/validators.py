import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .constants import (
    CNPJ_LENGTH,
    CPF_LENGTH
)


def validate_document(value: str):
    """Valida se o documento é um valor válido de CPF ou CNPJ"""

    value = re.sub(r"\D", "", value)  # Remove caracteres não numéricos

    if len(value) == CPF_LENGTH:
        if not validate_cpf(value):
            raise ValidationError(
                _("O CPF '{value}' é inválido.").format(value)
            )
    elif len(value) == CNPJ_LENGTH:
        if not validate_cnpj(value):
            raise ValidationError(
                _("O CNPJ '{value}' é inválido.").format(value)
            )
    else:
        raise ValidationError(
            _("Número deve ter {cpf} (CPF) ou {cnpj} (CNPJ) dígitos.").format(
                cpf=CPF_LENGTH,
                cnpj=CNPJ_LENGTH,
            )
        )


def validate_cpf(cpf: str) -> bool:
    if cpf == cpf[0] * CPF_LENGTH:
        return False

    def calculate_digit(cpf: str, weight: int) -> int:
        amount = sum(
            int(digit) * (weight - idx)
            for idx, digit in enumerate(cpf[: weight - 1])
        )
        rest = amount % 11
        return 0 if rest < 2 else 11 - rest

    first_digit = calculate_digit(cpf, 10)
    second_digit = calculate_digit(cpf, 11)
    return cpf[-2:] == f"{first_digit}{second_digit}"


def validate_cnpj(cnpj: str) -> bool:
    if cnpj == cnpj[0] * CNPJ_LENGTH:
        return False

    def calculate_digit(cnpj: str, pesos: list[int]) -> int:
        amount = sum(
            int(digit) * weight
            for digit, weight in zip(cnpj[: len(pesos)], pesos)
        )
        rest = amount % 11
        return 0 if rest < 2 else 11 - rest

    first_weight = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second_weight = [6] + first_weight

    first_digit = calculate_digit(cnpj, first_weight)
    second_digit = calculate_digit(cnpj, second_weight)

    return cnpj[-2:] == f"{first_digit}{second_digit}"
