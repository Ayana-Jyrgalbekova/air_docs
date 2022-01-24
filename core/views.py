import datetime

from django.db.models import Q, Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from core.forms import DocsForm
from core.models import Documents, Categories, Client


class DocsCreate(CreateView):
    model = Documents
    template_name = 'create.html'
    form_class = DocsForm
    success_url = '/home/'
    context_object_name = 'create'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['name'] = Client.objects.all()
        return context


class DocsUpdate(UpdateView):
    model = Documents
    template_name = 'update.html'
    form_class = DocsForm
    success_url = '/home/'
    context_object_name = 'create'


class DocsDetail(DetailView):
    queryset = Documents.objects.all()
    template_name = 'detail.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['is_check'] = self.object.date_answer == datetime.date.today()
        return context


class DocsList(ListView):
    queryset = Documents.objects.all()
    template_name = 'home.html'
    context_object_name = 'home'

    def get_queryset(self):
        query = self.request.GET.get('s', None)
        if query is None:
            return Documents.objects.all()

        return Documents.objects.filter(Q(text__icontains=query) | Q(date__icontains=query) | Q(id__icontains=query)
                                        | Q(date_answer__icontains=query)).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Categories.objects.all()
        return context


class Workers(ListView):
    queryset = Documents.objects.all()
    template_name = 'workers.html'
    context_object_name = 'workers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Documents.objects.values('fio__fio').annotate(count_fio=Count('fio'))
        context['docs'] = Documents.objects.count()
        context['client'] = Client.objects.all()
        return context


class CategoryFilter(ListView):
    template_name = 'category.html'
    context_object_name = 'categories'
    queryset = Documents.objects.all()

    def get_queryset(self):
        category_filter = self.queryset.filter(category__id=self.kwargs['pk'])
        return category_filter

