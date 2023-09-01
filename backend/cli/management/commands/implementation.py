import os

from cli.management.cli_base_command import CliBase
from django.conf import settings
from django.core.management.base import BaseCommand

base_stategy_file_raw_content: str = """
from django.db import models
from django_napse.core.models import Strategy


class {class_name}Strategy(Strategy):
    config = models.OneToOneField("{class_name}BotConfig", on_delete=models.CASCADE, related_name="strategy")
    architecture = models.OneToOneField(..., on_delete=models.CASCADE, related_name="strategy")

    def __str__(self) -> str:
        return f"{upper_name} BOT STRATEGY: {self.pk}"

    def info(self, verbose=True, beacon=""):
        string = ""
        string += f"{beacon}Strategy ({self.pk=}):\\n"
        string += f"{beacon}Args:\\n"
        string += f"{beacon}\\t{self.config=}\\n"
        string += f"{beacon}\\t{self.architecture=}\\n"
        if verbose:  # pragma: no cover
            print(string)
        return string
"""

base_config_file_raw_content: str = """
from django_napse.core.models import BotConfig


class {class_name}BotConfig(BotConfig):

    def __str__(self) -> str:
        return f"{upper_name} BOT CONFIG: {self.pk} - {self.immutable}"
"""


class Command(BaseCommand, CliBase):
    help = "Create a new architecture"

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Name of the new architecture file")

    def handle(self, *args, **kwargs):
        name = kwargs["name"]
        if not name:
            self.stdout.write(self.style.ERROR("Name cannot be empty or null"))
            self.stdout.write("Exiting...")
            raise SystemExit(1)

        root_dir: str = settings.ROOT_DIR
        directory: str = f"{root_dir}/custom/models/implementations/{name}"
        self.check_file_exists(directory)
        os.mkdir(directory)

        # Build __init__.py file
        init_filepath: str = directory + "/__init__.py"
        self.build_python_file(name=name, raw_content="\nfrom . import *", filepath=init_filepath)

        # Build strategy_file
        strategy_filepath: str = directory + "/strategy.py"
        self.build_python_file(
            name=name,
            raw_content=base_stategy_file_raw_content,
            filepath=strategy_filepath,
        )
        self.stdout.write(self.style.SUCCESS("/strategy python file created"))

        # Build config_file
        config_filepath: str = directory + "/config.py"
        self.build_python_file(
            name=name,
            raw_content=base_config_file_raw_content,
            filepath=config_filepath,
        )
        self.stdout.write(self.style.SUCCESS("/config python file created"))

        # Adjust rights
        os.chmod(directory, 0o777)  # noqa: S103
        os.chmod(init_filepath, 0o777)  # noqa: S103
        os.chmod(strategy_filepath, 0o777)  # noqa: S103
        os.chmod(config_filepath, 0o777)  # noqa: S103
