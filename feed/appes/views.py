from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from haystack.generic_views import FacetedSearchView as BaseFacetedSearchView
from haystack.query import SearchQuerySet
from django.shortcuts import get_object_or_404, render
import feedparser


from appes.models import Myfeed
from appes.forms import FacetedMyfeedSearchForm


class HomeView(TemplateView):
    template_name = "home.html"


class MyfeedView(DetailView):
    template_name = "product.html"
    model = Myfeed


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(
        content_auto=request.GET.get(
            'query',
            ''))[
        :5]
    s = []
    for result in sqs:
        d = {"value": result.title, "data": result.object.slug}
        s.append(d)
    output = {'suggestions': s}
    return JsonResponse(output)


class FacetedSearchView(BaseFacetedSearchView):

    form_class = FacetedMyfeedSearchForm
    facet_fields = ['category', 'main_link']
    template_name = 'search_result.html'
    paginate_by = 5
    context_object_name = 'object_list'
