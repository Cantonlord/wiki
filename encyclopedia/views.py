from django.shortcuts import render

from . import util


def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries()
    })

def wiki(request, title):
    content = util.get_entry(title)
    if content:
        return render(request, 'encyclopedia/entry.html', {
            'file': content
        })
    else:
        return render(request, 'encyclopedia/not-found.html')


