from django import template
register = template.Library()

# generally filter is used with {{}} and tags with {%%}
#filter takes only one argument while tags can take any number of arguments
#You can store the result of tag function call as template variable and use it
"""
Eg: {% concat "string" obj.attr obj2.attr as myvar %}
Eg: {{myvar}}
"""
#It is better to create tags since you can write in concise way your templates. 
#Filters increase the line length in templates
"""
#Tobe deleted. 
#Created a tag with same name - add_boolean_attr. 
#There is no need to delete,since there is no conflict 
#if you have a tag and a filter with same name.
#Just not to confuse in future, decided to delete.
@register.filter(name='add_boolean_attr')
def add_boolean_attr(exp, attr):
    #Tobe used for setting boolean attribute in html tag- like checked attribute in checkbox.
    #If exp true returns attr.
    #usage  : {{expr|add_boolean_attr:"<attr>"}}
    #example: {{task.done|add_boolean_attr:"checked"}}
    if(exp):
        return attr
    else:
        return ''
"""

@register.filter(name='get_related_query_set')
def get_related_query_set(rel_mgr):
    #filter to get related forieng key set
    #rel_mgr should be RelatedManager object.
    #In Many to one relationship, you get RelatedManager object by invoking qs.<forienkeyattr>_set
    return rel_mgr.all()


@register.simple_tag(name='add_boolean_attr')
def add_boolean_attr(exp, attr):
    #Tobe used for setting boolean attribute in html tag- like checked attribute in checkbox.
    #If exp true returns attr.
    """
    usage  : {% add_boolean_attr exp attr as result %}
    usage  : {{result}}
    example: {% add_boolean_attr item.done "checked" as output %}
    example: {{output}}
    """
    if(exp):
        return attr
    else:
        return ''

@register.simple_tag(name='concat')
def concat(*args):
    #tag to concat multiple template variables
    """
    usage  : {% concat obj.value obj.valu as result %}
    usage  : {{result}}
    Example: {% concat "string" obj.attr obj2.attr as myvar %}
    Example: {{myvar}}
    """
    result=""
    for obj in args:
        result+=str(obj)
    return result


