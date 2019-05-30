from django import template 

# Create the object
register = template.Library()

# Create the custom filter
# def cut(value,arg):
# 	"""
# 	This cuts out all values of 'arg' from the string
# 	"""
# 	return value.replace(arg,'')

# Register the function. 
# register.filter('cut',cut)

# First arg is the name that will be used for tagging, 
# the second arg is the name of the function itself



# Register cusom filters using Decorators
@register.filter(name='cut')
def cut(value,arg):
	"""
	This cuts out all values of 'arg' from the string
	"""
	return value.replace(arg,'')