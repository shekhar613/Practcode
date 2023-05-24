from django.urls import path
from . import views
from rest_framework.authtoken import views as authtoken_views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.userlogin, name='userlogin'),
    path('create', views.createUser, name='createUser'),
    path('dashboard', views.userDashboard, name='userDashboard'),
    path('testcase', views.testingCompiler, name='testingCompiler'),
    path('codeoutput', views.test_compilerCode, name='test_compilerCode'),
    path('mycourses', views.mycourses, name='mycourses'),
    
    # testing part
    path('user/',views.Authenticateuser.as_view()),
    path('register/',views.Registeruser.as_view()), #token auhtentication
    path('login/',views.LoginAuth_token.as_view()),
    # django JWT
    # path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh')
   
]
