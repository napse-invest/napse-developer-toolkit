import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Make a snapshot of custom plugins."

    def _add_snapshot_folder(self):
        """Add a snapshot folder to the custom plugins."""

        path: str = f"{os.getcwd()}/napse_dtk/snapshots"
        if not os.path.isdir(path):
            os.mkdir(path)

    def add_arguments(self, parser):
        parser.add_argument("--test", action="store_true")

    def handle(self, *args, **options):
        self._add_snapshot_folder()
        self.stdout.write(self.style.SUCCESS(f"Successfully made snapshot"))
