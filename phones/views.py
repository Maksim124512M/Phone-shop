from django.views import generic

from phones.models import Phone


class HomeView(generic.ListView):
    model = Phone
    template_name = 'phones/home.html'
    context_object_name = 'phones'
