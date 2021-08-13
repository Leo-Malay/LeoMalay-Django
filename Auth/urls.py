from django.urls import path
import Auth.views as views

urlpatterns = [
    path('', views.login, name='Login'),
    path('newAccount', views.newAccount, name='NewAccount'),
    path('forgotPass', views.forgotPass, name='ForgotPass'),
]
