from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, "pages/sample.html", {'page':page})

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Page

def page_edit(request, id):
    page = get_object_or_404(Page, id=id)
    if request.method == 'POST':
        page.title = request.POST['title']
        page.content = request.POST['content']
        page.save()
        return HttpResponseRedirect('/')
    return render(request, 'pages/sample.html', {'page':page})

