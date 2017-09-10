from django.shortcuts import render
from django.http import HttpResponseRedirect
from remember.models import Entry
from remember.forms import EntryForm
from urllib.parse import urlparse

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            link = form.cleaned_data['link']
            tag = form.cleaned_data['tag']
            desc = form.cleaned_data['desc']
            img = "http://logo.clearbit.com/" + urlparse(link).hostname + "?size=48"
            e = Entry(name=name, img=img, desc=desc, link=link, tag=tag)
            e.save()
            return HttpResponseRedirect('/')
    else:
        form = EntryForm()
        data = Entry.objects.all().order_by('-id')
        return render(request, "remember/main.html", {'data' : data, 'form': form})

def delete(request, id):
    e = Entry.objects.get(pk=id)
    e.delete()
    return HttpResponseRedirect('/')

def tag(request, tag):
    e = Entry.objects.filter(tag=tag)
    form = EntryForm()
    return render(request, "remember/main.html", {'data' : e, 'form': form})
