from django.conf.urls import patterns, url
from django.http import HttpResponse

from classlab.models import Poll

def stub(request, *args, **kwargs):
    return HttpResponse('stub view', mimetype="text/plain")

urlpatterns = patterns('djangor.views',
   (r"", "main"),
)
