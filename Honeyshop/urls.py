from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from shop.sitemaps import ProductSitemap



sitemaps = {
    'products': ProductSitemap,
}


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret-door/', admin.site.urls),

    # Allauth URL's
    path('accounts/', include('allauth.urls')),

    # Apps
    path('', include('shop.urls', namespace='shop')),
    path('', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
    
]

# ERROR 404- NOT FOUND PAGE
handler404 = 'shop.views.Erro404View'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    
