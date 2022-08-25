from django import template
register = template.Library()

@register.filter(name='add_boolean_attr')
def add_boolean_attr(exp, attr):
    """Tobe used with checkbox.If true returns checked."""
    if(exp):
        return attr
    else:
        return ''

@register.filter(name='get_related_query_set')
def get_related_query_set(rel_mgr):
    #filter to get related forieng key set
    #rel_mgr should be RelatedManager object.
    #In Many to one relationship, you get RelatedManager object by invoking qs.<forienkeyattr>_set
    return rel_mgr.all()
"""
@register.simple_tag(name='get_related_query_set')
def get_related_query_set(rel_mgr):
    #filter to get related forieng key set
    #rel_mgr should be RelatedManager object.
    #In Many to one relationship, you get RelatedManager object by invoking qs.<forienkeyattr>_set
    return rel_mgr.all()
"""
