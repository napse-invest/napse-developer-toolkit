import os
from importlib import import_module

from rest_framework.routers import DefaultRouter

main_api_router = DefaultRouter()

api_modules_folders_names = [
    elt for elt in os.listdir(os.path.dirname(__file__)) if os.path.isdir(os.path.join(os.path.dirname(__file__), elt)) and not elt.startswith("_")
]

for name in api_modules_folders_names:
    module = import_module(f"backend.api.{name}.urls")
    for elt in module.__dir__():
        instance = getattr(module, elt)
        if not elt.startswith("_") and isinstance(instance, DefaultRouter):
            main_api_router.registry.extend(instance.registry)
