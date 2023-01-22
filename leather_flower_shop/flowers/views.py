from django.template import loader
from django.http import HttpResponse


def flowers(request):
    template = loader.get_template('flowers.html')
    return HttpResponse(template.render())
