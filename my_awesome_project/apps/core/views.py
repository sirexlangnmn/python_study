from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from datetime import datetime


class HomeView(TemplateView):
    template_name = 'home.html'


def time_view(request):
    """HTMX endpoint for time demo."""
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return JsonResponse({'time': current_time})
