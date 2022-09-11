from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Books', views.BookView)
router.register('Category', views.CategoryView)
router.register('Signup', views.SignupView,basename='test')
router.register('Students', views.StudentsView)


urlpatterns = [
    path('', include(router.urls)),
    path('login/',views.LoginView.as_view())
]