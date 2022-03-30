from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util, forms
import random

form = forms.SearchForm()

def index(request):
    return render(request, 'encyclopedia/index.html', {
        'entries': util.list_entries(),
        'form': form
    })

def entry(request, title):
    content = util.get_entry(title)
    if content:
        return render(request, 'encyclopedia/entry.html', {
            'content': content,
            'form': form
        })
    else:
        return render(request, 'encyclopedia/error.html', {
            'form': form
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
                    'form': form
                })
            
            elif len_results == 1 and results[0].lower() == query:
                return HttpResponseRedirect(reverse('entry', args=[query]))

            else:
                result = [result for result in results if query == result.lower()]

                if len(result) > 0:
                    return HttpResponseRedirect(reverse('entry', args=[query]))
                else:
                    return render(request, 'encyclopedia/result.html', {
                        'multi_results': f'{len_results} results found',
                        'results': results,
                        'form': form
                    })
        else:
            return HttpResponseRedirect(reverse('index'))