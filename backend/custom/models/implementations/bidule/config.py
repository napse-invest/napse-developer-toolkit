from django_napse.core.models import BotConfig


class BiduleBotConfig(BotConfig):

    def __str__(self) -> str:
        return f"BIDULE BOT CONFIG: {self.pk} - {self.immutable}"
