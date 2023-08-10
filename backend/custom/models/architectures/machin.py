
from django_napse.core import Architecture


class MachinArchitecture(Architecture):

    def __str__(self) -> str:
        return f"MACHIN ARCHITECHTURE {self.pk}"

    def info(self, verbose=True, beacon=""):
        string = ""
        string += f"{beacon}Machin Architecture {self.pk}:\n"

        if verbose:  # pragma: no cover
            print(string)
        return string
