from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import(
        DetailView, DeleteView, UpdateView, CreateView, ListView)
from django.views.generic.dates import DayArchiveView, DateDetailView, ArchiveIndexView
from .forms import SalesForm, ProductsForm
from .models import Sold, Products

# Create a login url so you are directed to it
class LockedView(LoginRequiredMixin):
    login_url = "admin:login"

# Creates a view of list of available products remaining
class ProductsListView(ListView):
    model = Products
    #queryset = Products.objects.all()
    template_name = 'sales/product_list.html'

class ProductEntryView(CreateView):
    model = Products
    #fields = ['product_name']
    #template_name = 'sales/product_form.html'
    form_class = ProductsForm

class ProductsDetailView(DetailView):
    model = Products
    template_name = 'sales/product_detail.html'
    slug_field = 'pk'
    slug_url_kwarg = 'product_detail'

    #def get_context_data(self, **kwargs):
        #context = super(ProductsDetailView, self).get_context_data(**kwargs)
        #return context
    #def get_queryset(self):
        #return Products.objects.all()

class ProductsDeleteView(DeleteView):
    model= Products
    template_name = 'sales/product_confirm_delete.html'
    success_url = reverse_lazy('products-list')

class ProductsUpdateView(UpdateView):
    model = Products
    fields=['product_name', 'quantity', 'expiry_date'] 
    success_url = reverse_lazy('products-list')

# Creates a view of list of products sold 
class SoldIndexView(ArchiveIndexView):
    model = Sold
    date_field = 'date'
    template_name = 'sales/sold_list.html'
    date_list_period = 'day'
    #queryset = Sold.objects.filter(date__day=17)

    
    def get_context_data(self, **kwargs):
        context = super(SoldIndexView, self).get_context_data(**kwargs)
        months = Sold.objects.dates('date', 'day', order='DESC')
        context['months'] = months
        return context

# Creates day view of products
class SoldDayArchiveView(DayArchiveView):
    queryset = Sold.objects.all() # same as model = Sold
    date_field = 'date'
    allow_future = False
    #paginate_by = 5

    def listing(request):
        daily_sale = Sold.objects.all()
        paginator = Paginator(daily_sale, 5) #Show 5 sales record per page

        page_number = request.Get.get('page')
        page_obj =  paginator.get_page(page_number)
        return render(request, 'sold_archive_day.html', {'page_obj': page_obj})


class SoldDateDetailView(DateDetailView):
    queryset = Sold.objects.all()

# Creates a form for entering records
class SoldEntryView(CreateView):
    model = Sold
    form_class = SalesForm

# Updates the field in a form
class SoldUpdateView(UpdateView):
    model = Sold
    fields = ['date', 'product_name', 'quantity_sold', 'unit_price', 'total', 'note']
    success_url = reverse_lazy('sold-dates-list')

# Deletes a sale entry
class SoldDeleteView(DeleteView):
    model = Sold
    success_url = reverse_lazy('sold-dates-list')
