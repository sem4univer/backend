from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets, permissions
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


from drf_yasg import openapi
from django.contrib import admin

from shop.views import ProductViewSet, ReviewViewSet

from auth.views import AuthViewSet


admin.autodiscover()

schema_view = get_schema_view(openapi.Info(
    title='Online shop API',
    default_version='v1',
    description='This is api for online shop',
    terms_of_service='https://www.google.com/policies/terms/',
    contact=openapi.Contact(email='sasazhava13@gmail.com'),
    license=openapi.License(name='BSD License'),
),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()

router.register('products', ProductViewSet, basename='product')
router.register('review', ReviewViewSet, basename='review')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.social.urls')),
    path('vk-login', AuthViewSet.as_view()),
    path('', include('social_django.urls')),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)