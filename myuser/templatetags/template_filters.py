from django import template
register = template.Library()

@register.filter(name='add_class')
def add_class(exp, class_name):
    """If exp is true then returns class_name"""
    if(exp):
        return class_name
    else:
        return ''
@register.simple_tag(name='get_error_msg')
def get_error_msg(separator,form_errors,default):
    #Separator to be used when joining the list elements
    #form_error should be list. eg:form.email.errors
    #Default string to return if form.fields.errors list is empty
    #return concated errors in a single string joined by separators
    if(form_errors):
        return separator.join(form_errors)
    else:
        return default

@register.simple_tag(name='conditional_value')
def conditional_value(condition,truth_value,false_value):
    if(condition):
        return truth_value
    else:
        return false_value

