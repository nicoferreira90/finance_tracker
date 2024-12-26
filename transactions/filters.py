import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):

    transaction_type = django_filters.ChoiceFilter(choices=Transaction.TRANSACTION_TYPE)

    class Meta:
        model = Transaction
        fields = ['type']