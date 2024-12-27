from django.shortcuts import render
from django.views.generic import ListView
from .filters import TransactionFilter

from .models import Transaction

class TransactionListView(ListView):
    model = Transaction
    template_name = "transactions/transaction_list.html"
    context_object_name = "transactions"
    paginate_by = 100

    def get_queryset(self):
        queryset = super().get_queryset()
        transaction_filter = self.request.GET.get("type")
        if transaction_filter:
            queryset = queryset.filter(type=transaction_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transaction_filter = TransactionFilter(self.request.GET, queryset=self.get_queryset())
        context["filter"] = transaction_filter
        return context