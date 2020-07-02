import markdown2
from markdown2 import Markdown

from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import util


def index(request):
    if request.method == "POST":
        name = request.POST.get('q')
        title = name
        markdowner = Markdown()
        name = util.get_entry(name)
        name = markdowner.convert(name)
        return render(request, "encyclopedia/entry.html", {
        "name": name,
        "title": title
        })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    markdowner = Markdown()
    title = name
    name = util.get_entry(name)
    name = markdowner.convert(name)
    return render(request, "encyclopedia/entry.html", {
    "name": name,
    "title": title
    })

def results(request):
    return('stuff')
