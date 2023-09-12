from django.views.generic import(
    ListView,
    CreateView,
    UpdateView,

)

from .models import Card
from django.urls import reverse_lazy

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")


class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box" ]
    success_url = reverse_lazy("card-create")



