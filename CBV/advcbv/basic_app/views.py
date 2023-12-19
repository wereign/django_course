from typing import Any
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

class CBV(View):
    def get(self,request):
        return HttpResponse("Class Based Views Worked")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'

        return context
