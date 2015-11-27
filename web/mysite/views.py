from django.shortcuts import render
from django.shortcuts import redirect, render_to_response, render
from django.template import Context, RequestContext
from django.http import HttpResponse

# Create your views here.

def entry(request):
#    return HttpResponse("Hello world")
    return redirect('/blog')

def hello(request):
    return HttpResponse("Hello world")

def about(request):
#    return render_to_response('xabout.html', locals(), RequestContext(request))
    return render_to_response('about.html', locals(), RequestContext(request))
