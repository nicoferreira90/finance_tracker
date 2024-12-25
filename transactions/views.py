from django.shortcuts import render
from django.views.generic import ListView

from .models import Transaction

class TransactionListView(ListView):
    model = Transaction
    template_name = "transactions/transaction_list.html"
    context_object_name = "transactions"
    paginate_by = 10

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by("-date")
