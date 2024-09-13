from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from phones.models import Phone, Order, Basket, PhoneReview
from phones.forms import CreateOrder, AddReviewForm


class HomeView(generic.ListView):
    model = Phone
    template_name = 'phones/home.html'
    context_object_name = 'phones'


class PhoneDetailView(generic.DetailView, generic.FormView):
    model = Phone
    template_name = 'phones/phone-detail.html'
    context_object_name = 'phone'
    form_class = AddReviewForm
    success_url = reverse_lazy('phones:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = PhoneReview.objects.filter(product_id=self.kwargs.get('pk')).order_by('-date')

        return context

    def form_valid(self, form):
        form.instance.product = Phone.objects.get(id=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)


class ReviewDeleteView(generic.DeleteView):
    model = PhoneReview
    template_name = 'phones/review-delete.html'
    success_url = reverse_lazy('phones:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = PhoneReview.objects.get(id=self.kwargs.get('pk'))

        return context


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


class BasketView(LoginRequiredMixin, generic.ListView):
    template_name = 'phones/basket.html'
    model = Basket
    context_object_name = 'baskets'

    def get_queryset(self):
        baskets = Basket.objects.filter(owner=self.request.user)

        return baskets


@login_required
def add_product_in_basket(request, pk):
    product = Phone.objects.get(id=pk)
    basket = Basket.objects.filter(product=product, owner=request.user)
    
    Basket.objects.create(
        product=product,
        owner=request.user
    )
    # basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
    
