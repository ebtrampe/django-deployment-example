from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING PURPOSES
# create a variable name called app_name which will be specified in the relative_urls_templates.html file
app_name = 'basic_app'

urlpatterns = [
	# this is basically saying, domain.com/basic_app/relative/
	url(r'^relative/$',views.relative,name='relative'),
	url(r'^other/$',views.other,name='other'),
]