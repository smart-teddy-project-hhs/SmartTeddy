from django.views.decorators.http import require_POST
from django.http import HttpResponse


def index(request):
    return 404


@require_POST
def sentence(request):
    pass
