import inspect
import os

from django.conf import settings


class CliBase:
    def _create_file_content(self, name: str, raw_content: str) -> str:
        content = "\n".join(raw_content.split("\n")[1:])
        content = content.replace("{class_name}", name.capitalize().replace("_", ""))
        content = content.replace("{lower_name}", name.lower())
        content = content.replace("{upper_name}", name.upper().replace("_", " "))
        return content.replace("{title_name}", name.capitalize().replace("_", " "))

    def build_python_file(self, name: str, raw_content: str, filepath: str = "") -> None:
        root_dir: str = settings.ROOT_DIR
        directory: str = f"{root_dir}/custom/models/{inspect.getfile(self.__class__).split('/')[-1].split(('.'))[0]}s"
        filepath: str = filepath or f"{directory}/{name}.py"

        self.check_file_exists(filepath)

        with open(filepath, "w") as file:
            file.write(self._create_file_content(name=name, raw_content=raw_content))
        file.close()

    def check_file_exists(self, filepath: str) -> None:
        if os.path.exists(filepath):
            self.stdout.write(self.style.ERROR(f"{filepath} already exists"))
            self.stdout.write("Exiting...")
            raise SystemExit(1)
