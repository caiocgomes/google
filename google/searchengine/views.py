from django.shortcuts import render_to_response,render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from google.searchengine.web_search import google
from google.searchengine.web_search import Phonetize
from google.searchengine.web_search import SearchTest

@csrf_exempt
def search(request):

    if request.POST:
		#render_to_response('search.html', {'result': caio(request.POST['term'], 10)})
		#print request.POST['term']
		#print request.POST['teste1']
		return render_to_response('search.html', {'result': SearchTest(request.POST['term'],30)})
		#return render_to_response('search.html', {'result': google(request.POST['term'], 10)})
		#return HttpResponseRedirect("/")
    else:
		return render_to_response('search.html')