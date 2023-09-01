from cli.management.cli_base_command import CliBase
from django.core.management.base import BaseCommand

base_architecture_file_raw_content: str = """
from django_napse.core.models import Architecture


class {class_name}Architecture(Architecture):

    def __str__(self) -> str:
        return f"{upper_name} ARCHITECHTURE {self.pk}"

    def info(self, verbose=True, beacon=""):
        string = ""
        string += f"{beacon}{title_name} Architecture {self.pk}:\\n"

        if verbose:  # pragma: no cover
            print(string)
        return string
"""


class Command(BaseCommand, CliBase):
    help = "Create a new architecture"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Name of the new architecture file")

    def handle(self, *args, **kwargs):
        self.setup_folder()

        name = kwargs["name"]
        if not name:
            self.stdout.write(self.style.ERROR("Name cannot be empty or null"))
            self.stdout.write("Exiting...")
            raise SystemExit(1)

        self.build_python_file(name=name, raw_content=base_architecture_file_raw_content)
        self.stdout.write(self.style.SUCCESS(f"{name} python file created"))
