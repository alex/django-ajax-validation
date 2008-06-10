from django import template

register = template.Library()

def include_validation():
    return '''
    <script type="text/javascript">
        (function($)    {
            function inputs(form)   {
                return form.find("input[@checked], input[@type='text'], input[@type='hidden'], input[@type='password'], input[@type='submit'], option[@selected], textarea").filter(':enabled');
            }
            
            $.fn.validate = function(url, settings) {
                settings = $.extend({
                    type: 'table'
                }, settings);
                
                return this.each(function() {
                    $(this).submit(function()  {
                        var form = $(this);
                        var params = {};
                        inputs($(this)).each(function() {
                            params[ this.name || this.id || this.parentNode.name || this.parentNode.id ] = this.value; 
                        });
                        
                        var status = false;
                        $.ajax({
                            async: false,
                            data: params,
                            dataType: 'json',
                            error: function(XHR, textStatus, errorThrown)   {
                                status = true;
                            },
                            success: function(data, textStatus) {
                                status = data.valid;
                                if (!status)    {
                                    if (settings.type == 'p')    {
                                        inputs(form).parent().prev('ul').remove();
                                        inputs(form).parent().prev('ul').remove()
                                        $.each(data.errors, function(key, val)  {
                                            if (key == '__all__')   {
                                                var error = inputs(form).filter(':first').parent();
                                                if (error.prev().is('ul.errorlist')) {
                                                    error.prev().before('<ul class="errorlist"><li>' + val + '</li></ul>');
                                                }
                                                else    {
                                                    error.before('<ul class="errorlist"><li>' + val + '</li></ul>');
                                                }
                                            }
                                            else    {
                                                $('#id_' + key).parent().before('<ul class="errorlist"><li>' + val + '</li></ul>');
                                            }
                                        });
                                    }
                                    if (settings.type == 'table')   {
                                        inputs(form).prev('ul').remove();
                                        $.each(data.errors, function(key, val)  {
                                            $('#id_' + key).before('<ul class="errorlist"><li>' + val + '</li></ul>');
                                        });
                                    }
                                    if (settings.type == 'ul')  {
                                        inputs(form).prev().prev('ul').remove();
                                        $.each(data.errors, function(key, val)  {
                                            $('#id_' + key).prev().before('<ul class="errorlist"><li>' + val + '</li></ul>');
                                        });
                                    }
                                }
                            },
                            type: 'POST',
                            url: url
                        });
                        return status;
                    });
                });
            };
        })(jQuery);
    </script>
    '''
register.simple_tag(include_validation)
