import contextlib
import os
import re
from importlib import import_module

from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import GenericViewSet


def build_main_router() -> DefaultRouter:
    main_router = DefaultRouter()

    api_modules_folders_names = [
        elt
        for elt in os.listdir(os.path.dirname(__file__))
        if os.path.isdir(os.path.join(os.path.dirname(__file__), elt)) and not elt.startswith("_")
    ]

    for name in api_modules_folders_names:
        module = import_module(f"api.{name}.views")
        for elt in module.__dir__():
            if elt.startswith("_"):
                continue

            instance = getattr(module, elt)

            with contextlib.suppress(TypeError):
                if issubclass(instance, GenericViewSet):
                    # from CamelCase to snake_case & remove "_view" (ex: MyWalletView -> my_wallet)
                    print(f"\n\nNAME: {instance.__name__}")
                    url_name = "_".join(re.sub("([a-z0-9])([A-Z])", r"\1_\2", instance.__name__).lower().split("_")[:-1])
                    print("main url", main_router.urls)
                    main_router.register(url_name, instance, basename=url_name)
                    print("main url", main_router.urls)
    return main_router


main_api_router = build_main_router()
print("\n\nurl", main_api_router.urls)
