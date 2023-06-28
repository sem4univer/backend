from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import routers, serializers, viewsets

from rest_framework_swagger.views import get_swagger_view

from shop.views import ProductViewSet, ReviewViewSet

schema_view = get_swagger_view(title='Pastebin API')


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register('products', ProductViewSet, basename='product')
router.register('review', ReviewViewSet, basename='review')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('docs', schema_view),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
