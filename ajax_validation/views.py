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
        data = {
            'valid': False,
            'errors': form.errors,
        }
    json_serializer = LazyEncoder()
    return HttpResponse(json_serializer.encode(data), mimetype='application/json')
validate = require_POST(validate)
