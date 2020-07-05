
import markdown2
from markdown2 import Markdown

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect



from . import util

def index(request):
    if request.method == "POST":
        name = request.POST.get('q')
        title = name
        markdowner = Markdown()
        name = util.get_entry(title)
        stuff = util.list_entries()
        try:
            name = markdowner.convert(name)
            return redirect('/wiki/' + title)
        except:
            for text in stuff:
                if title in text:
                    print("Partial match")
                    print(text)
                    return render(request, "encyclopedia/results.html", {
                        "text": text
                        })
        if name == None:
            return render(request, "encyclopedia/index.html", {
            "msg": 'Error: The requested page does not exist'
            })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    markdowner = Markdown()
    edit = name
    title = name
    name = util.get_entry(name)
    try:
        name = markdowner.convert(name)
    except:
        return render(request, "encyclopedia/index.html", {
        "msg": 'Error: The requested page does not exist'
        })
    if request.method == "POST" and request.POST.get('ser') == 'ser':
        name = request.POST.get('q')
        title = name
        markdowner = Markdown()
        name = util.get_entry(title)
        stuff = util.list_entries()
        try:
            name = markdowner.convert(name)
            return redirect('/wiki/' + title)
        except:
            for text in stuff:
                if title in text:
                    print("Partial match")
                    print(text)
                    return render(request, "encyclopedia/results.html", {
                        "text": text
                        })

    elif request.method == "POST" and request.POST.get('edit') == 'edit':
        return redirect('/wiki/' + edit + '/edit/')


    return render(request, "encyclopedia/entry.html", {
    "name": name,
    "title": title
    })

def create(request):
    print('create')
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        stuff = util.list_entries()
        if title in stuff:
            print("Entry title taken")
            return render(request, "encyclopedia/create.html", {
            "msg": f"A page with that entry name already exists at <a href='/wiki/{title}'>{title}</a>."
            })
        else:
            util.save_entry(title, content)
            return redirect('/wiki/' + title)
    return render(request, "encyclopedia/create.html")

def edit(request, name):
    print(name)
    title = name
    content = util.get_entry(name)
    if request.method == "POST":
        content = request.POST.get('content')
        util.save_entry(title, content)
        return redirect('/wiki/' + title)
    return render(request, "encyclopedia/edit.html", {
    "title": title,
    "content": content
    })

def random(request):
    import random
    rand = util.list_entries()
    title = random.choice(rand)
    print(title)
    return redirect('/wiki/' + title)
