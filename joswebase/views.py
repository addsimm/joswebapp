# Create your views here.
from __future__ import print_function

from django.shortcuts import render_to_response
from django.template.context import RequestContext


def tempindex(request):
    context = RequestContext(request,
                           {'request': request,
                            'user'   : request.user})
    return render_to_response('login.html', context_instance=context)