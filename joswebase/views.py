# Create your views here.
from __future__ import print_function

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext


def tempindex(request):
    template_values = {}
    current_user = ''  ##### find current user
    context = RequestContext(request, template_values)
    context.update({'page_name': 'Landing Page',
                    'user': current_user
                    })
    return render_to_response('tempindex.html', context)