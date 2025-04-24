from django.db import models
from django.utils.translation import gettext_lazy as _

from .constants import (
    DOCUMENT_MAX_LENGTH,
)
from .validators import (
    validate_document,
)
from .utils import format_document


class DocumentField(models.CharField):
    """Field document for CPF or CNPJ with validation"""

    description = "Field document for CPF or CNPJ with validation"

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = DOCUMENT_MAX_LENGTH
        kwargs["help_text"] = _("O documento deve ser um CPF ou CNPJ válido")
        kwargs["verbose_name"] = _("Documento")

        validators = kwargs.get("validators", [])

        if validate_document not in validators:
            validators.append(validate_document)

        kwargs["validators"] = validators
        super().__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)

        def get_display(instance):
            value = getattr(instance, name)
            return format_document(value)

        setattr(cls, f"get_{name}_display", get_display)
