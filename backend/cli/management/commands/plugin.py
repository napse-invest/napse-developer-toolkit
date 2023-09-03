from cli.management.cli_base_command import CliBase
from django.core.management.base import BaseCommand

base_plugin_file_raw_content: str = """
from django_napse.core.models import Plugin
from django_napse.core.models import ConnectionSpecificArgs
from django_napse.utils.constants import PLUGIN_CATEGORIES, SIDES


class {class_name}Plugin(Plugin):
    @classmethod
    def plugin_category(cls):
        # must return one of the PLUGIN_CATEGORIES
        ...

    def _apply(self, data: dict) -> dict:
        order = data["order"]
        if order["side"] == SIDES.BUY:
            ...
        if order["side"] == SIDES.SELL:
            ...
        return data

    def _connect(self, connection):
        ConnectionSpecificArgs.objects.create(connection=connection, key="{lower_name}", value=..., target_type=...)
"""


class Command(BaseCommand, CliBase):
    help = "Create a new plugin"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Name of the new plugin")

    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        if not name:
            self.stdout.write(self.style.ERROR("Name cannot be empty or null"))
            self.stdout.write("Exiting...")
            raise SystemExit(1)

        self.build_python_file(name=name, raw_content=base_plugin_file_raw_content)
        self.stdout.write(self.style.SUCCESS(f"{name} python file created"))
