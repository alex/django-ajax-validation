from ajax_validation.utils import LazyEncoder
from django.http import HttpResponse
from django.views.decorators.http import require_POST

def validate(request, *args, **kwargs):
    form_class = kwargs.pop('form_class')
    extra_args_func = kwargs.get('callback', lambda request, *args, **kwargs: {})
    kwargs = extra_args_func(request, *args, **kwargs)
    form = form_class(request.POST, request.FILES, **kwargs)
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
