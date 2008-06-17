from ajax_validation.utils import LazyEncoder
from django.http import HttpResponse
from django.views.decorators.http import require_POST

def validate(request, form_class):
    form = form_class(request.POST, request.FILES)
    if form.is_valid():
        data = {
            'valid': True,
        }
    else:
        if request.POST.getlist('fields'):
            fields = request.POST.getlist('fields') + ['__all__']
            errors = dict([(key, val) for key, val in form.errors.iteritems() if key in fields])
        else:
            errors = form.errors
        data = {
            'valid': False,
            'errors': errors,
        }
    json_serializer = LazyEncoder()
    return HttpResponse(json_serializer.encode(data), mimetype='application/json')
validate = require_POST(validate)
