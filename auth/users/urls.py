from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileSet)

urlpatterns = router.urls
urlpatterns += [
        path('', views.index, name='index'),
        path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
        path('register/', views.CreateUserView.as_view()),
        path('myprofile/', views.SingleUserProfileDetail.as_view()),
]

