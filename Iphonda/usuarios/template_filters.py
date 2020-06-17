from django.template.base import Library  

register = Library()  
 
@register.filter 
def get_item(dictionary, key):     
    return dictionary.get(key)