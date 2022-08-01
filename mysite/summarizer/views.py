from django.shortcuts import render
from .models import SearchQuery
from django.http import HttpResponse
from .forms import SearchQueryForm


def index(request):
    form = SearchQueryForm()
    context = {'form': form}
    return render(request, 'summarizer/index.html', context)
