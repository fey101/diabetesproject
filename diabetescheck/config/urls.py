"""config URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from diabetescheck_auth.views import MeView
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^o/',
        include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^me/$', MeView.as_view(), name='me'),
    url(r'^accounts/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/',
        include('diabetescheck_auth.urls', namespace='auth')),
    url(r'^api/recipe/',
        include('recipe.urls', namespace='recipe')),
    # url(r'^api/planner/',
    #     include('planner.urls', namespace='planner')),
    url(r'^api/journal/',
        include('journal.urls', namespace='journal')),
    url(r'^api/community/',
        include('community.urls', namespace='community'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
