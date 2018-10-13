"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.conf.urls.static import static

from django.views.generic import RedirectView

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    # url(r"^ratings/", include("pinax.ratings.urls", namespace="pinax_ratings")),
]

# we just appended a new list item using the += operator to clearly separate the old and new code)
urlpatterns += [
    path('catalog/', include('catalog.urls')),
    # url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

]

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog')),
]
#pattern for static file link:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
# for static file link:

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


