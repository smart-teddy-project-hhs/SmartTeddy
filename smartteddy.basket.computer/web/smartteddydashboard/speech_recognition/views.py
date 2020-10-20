from django.views.decorators.http import require_POST
from django.http import HttpResponse


@require_POST
def sentence(request):
    return HttpResponse("hello world")
