from django.db import models
from django_napse.core.models import Strategy


class BiduleStrategy(Strategy):
    config = models.OneToOneField("BiduleBotConfig", on_delete=models.CASCADE, related_name="strategy")
    architecture = models.OneToOneField(..., on_delete=models.CASCADE, related_name="strategy")

    def __str__(self) -> str:
        return f"BIDULE BOT STRATEGY: {self.pk}"

    def info(self, verbose=True, beacon=""):
        string = ""
        string += f"{beacon}Strategy ({self.pk=}):\n"
        string += f"{beacon}Args:\n"
        string += f"{beacon}\t{self.config=}\n"
        string += f"{beacon}\t{self.architecture=}\n"
        if verbose:  # pragma: no cover
            print(string)
        return string
