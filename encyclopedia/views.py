from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util, forms
import random, markdown2

search_form = forms.SearchForm()
create_form = forms.CreateForm()

def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries(),
        'form': search_form
    })

def entry(request, title):
    content = util.get_entry(title)
    if content:
        return render(request, 'encyclopedia/entry.html', {
            'content': markdown2.markdown(content),
            'form': search_form
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            'form': search_form
        })

def search(request):
    if request.method == 'GET':
        form = forms.SearchForm(request.GET)
        
        if form.is_valid():
            query = form.cleaned_data['q'].lower()
            entries = util.list_entries()

            results = [result for result in entries if query in result.lower()]
            len_results = len(results)
            print(f'len_results: {len_results}')
            # No matching result found
            if len_results == 0:
                return render(request, 'encyclopedia/result.html', {
                    'none_result': 'No results found',
                    'form': search_form
                })
            
            elif len_results == 1 and results[0].lower() == query:
                return HttpResponseRedirect(reverse('entry', args=[query]))

            else:
                result = [result for result in results if query == result.lower()]

                if len(result) > 0:
                    return HttpResponseRedirect(reverse('entry', args=[query]))
                else:
                    return render(request, 'encyclopedia/result.html', {
                        'multi_results': f'{len_results} result(s) found',
                        'results': results,
                        'form': search_form
                    })
        else:
            return HttpResponseRedirect(reverse('index'))


def create(request):
    if request.method == 'POST':
        form = forms.CreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            entries = util.list_entries()
            for entry in entries:
                if entry.lower() == title.lower():
                    return render(request, 'encyclopedia/create.html', {
                       'create_form': create_form,
                       'form': search_form,
                       'error': 'This page has already been created!'
                    })
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('entry', args=[title]))
    else:
        return render(request, 'encyclopedia/create.html', {
            'create_form': create_form,
            'form': search_form
        })