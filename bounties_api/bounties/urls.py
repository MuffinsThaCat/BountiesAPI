"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.views.generic.base import TemplateView
from django.conf.urls import url, include
from django.contrib import admin
from bounties.views import custom_sitemap_index
from bounties.sitemaps import BountyMap, ProfileMap, StaticMap
from rest_framework_swagger.renderers import (
    SwaggerUIRenderer,
    OpenAPIRenderer
)

# Rendering for Swagger
schema_view = get_schema_view(title='Bounties API', renderer_classes=[
    OpenAPIRenderer, SwaggerUIRenderer])

sitemaps = {
    'BountyMap': BountyMap,
    'ProfileMap': ProfileMap,
    'StaticMap': StaticMap
}

urlpatterns = [
    url(r'^sitemap\.xml$', custom_sitemap_index,
        {'sitemaps': sitemaps}, name='custom_sitemap_index'),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('user.auth_urls', namespace='auth')),
    url(r'^user/', include('user.user_urls', namespace='user')),
    url(r'^notification/', include('notifications.urls', namespace='notification')),
    url(r'^analytics/', include('analytics.urls', namespace='analytics')),
    url(r'^', include('std_bounties.urls', namespace='std_bounties')),
]
