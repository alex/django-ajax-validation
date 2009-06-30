from django import forms
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.forms.formsets import BaseFormSet

from ajax_validation.utils import LazyEncoder

def validate(request, *args, **kwargs):
    form_class = kwargs.pop('form_class')
    extra_args_func = kwargs.pop('callback', lambda request, *args, **kwargs: {})
    kwargs = extra_args_func(request, *args, **kwargs)
    kwargs['data'] = request.POST
    form = form_class(**kwargs)
    if form.is_valid():
        data = {
            'valid': True,
        }
    else:
        # if we're dealing with a FormSet then walk over .forms to populate errors and formfields
        if isinstance(form, BaseFormSet):
            errors = {}
            formfields = {}
            for f in form.forms:
                for fieldname in f.fields.keys():
                    formfields['%s-%s' % (f.prefix, fieldname)] = f[fieldname]
                for field, error in f.errors.iteritems():
                    errors['%s-%s' % (f.prefix, field)] = error
        else:
            errors = form.errors
            formfields = dict([(fieldname, form[fieldname]) for fieldname in form.fields.keys()])

        # if fields have been specified then restrict the error list
        if request.POST.getlist('fields'):
            fields = request.POST.getlist('fields') + ['__all__']
            errors = dict([(key, val) for key, val in errors.iteritems() if key in fields])

        final_errors = {}
        for key, val in errors.iteritems():
            if key == '__all__':
                final_errors['__all__'] = val
            elif not isinstance(formfields[key].field, forms.FileField):
                html_id = formfields[key].field.widget.attrs.get('id') or formfields[key].auto_id
                html_id = formfields[key].field.widget.id_for_label(html_id)
                final_errors[html_id] = val
        data = {
            'valid': False,
            'errors': final_errors,
        }
    json_serializer = LazyEncoder()
    return HttpResponse(json_serializer.encode(data), mimetype='application/json')
validate = require_POST(validate)
