from django_napse.core.models import BinanceAccount, Exchange, ExchangeAccount
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# from rest_framework.decorators import action


class ExchangeView(GenericViewSet):
    permission_classes = []

    def list(self, request):
        print(Exchange.objects.all())
        print(ExchangeAccount.objects.all())
        print(BinanceAccount.objects.all())
        return Response(status=status.HTTP_200_OK)
