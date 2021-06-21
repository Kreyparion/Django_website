"""cmix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from pages import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

handler404 = 'pages.views.error404_view'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home/', views.home_view, name='home'),
    path('administration_login/', admin.site.urls),
    path('presta/', include('presta.urls'), name='presta'),
    path('reseaux/', views.reseaux_view, name='reseaux'),
    path('medias/', views.medias_view, name='medias'),
    path('playlist/', views.playlist_view, name='playlist'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
# Superuser : CMIXadmin2021 / Js1AIsstI@u2nG (Je suis 1 Admin I solemny swear that I @m up 2 no Good)
