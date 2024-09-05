from django.views import generic
from django.urls import reverse_lazy

from phones.models import Phone, Order
from phones.forms import CreateOrder


class HomeView(generic.ListView):
    model = Phone
    template_name = 'phones/home.html'
    context_object_name = 'phones'


class PhoneDetailView(generic.DetailView):
    model = Phone
    template_name = 'phones/phone-detail.html'
    context_object_name = 'phone'


class CreateOrder(generic.CreateView):
    model = Order
    form_class = CreateOrder
    template_name = 'phones/create-order.html'
    success_url = reverse_lazy('phones:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = Phone.objects.get(id=self.kwargs.get('pk'))
        
        return context

    def form_valid(self, form):
        phone = Phone.objects.get(id=self.kwargs.get('pk'))
        form.instance.product = phone
        
        return super().form_valid(form)
