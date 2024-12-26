from django.shortcuts import render
from django.views.generic import ListView
from .filters import TransactionFilter

from .models import Transaction

class TransactionListView(ListView):
    model = Transaction
    template_name = "transactions/transaction_list.html"
    context_object_name = "transactions"
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        transaction_filter = TransactionFilter(request.GET, queryset=self.object_list)
        context = self.get_context_data(object_list=self.object_list, **kwargs)
        context["filter"] = transaction_filter
        return self.render_to_response(context)


    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by("-date")
