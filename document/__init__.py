from django.utils.module_loading import autodiscover_modules

from montseguro.core.registry import module_registry


def autodiscover():
    autodiscover_modules("module", register_to=module_registry)
