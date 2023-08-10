import inspect

from django.conf import settings


class CliBase:
    def _create_file_content(self, name: str, raw_content: str) -> str:
        content = raw_content
        content = content.replace("{class_name}", name.capitalize().replace("_", ""))
        content = content.replace("{lower_name}", name.lower())
        content = content.replace("{upper_name}", name.upper().replace("_", " "))
        return content.replace("{title_name}", name.capitalize().replace("_", " "))

    def build_python_file(self, module_name: str, name: str, raw_content: str) -> None:
        root_dir = settings.ROOT_DIR
        directory = f"{root_dir}/custom/models/{inspect.getfile(self.__class__).split('/')[-1].split(('.'))[0]}s"

        with open(f"{directory}/{name}.py", "w") as file:
            file.write(self._create_file_content(name=name, raw_content=raw_content))
        file.close()
