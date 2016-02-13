from django.conf.urls import url
from django.contrib.auth.views import logout, password_change

from . import views

urlpatterns = [
    url(r'^login/$', views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url('^change-password/$', password_change, {
        'template_name': 'accounts/change_password.html',
        'post_change_redirect': '/',
    }, name='change-password'),

    url(r'^register/', views.RegisterView.as_view(), name='register'),

    url(r'^profile/', views.UserDetail.as_view(), name='user-profile'),
    url(r'^user/edit/', views.UserEdit.as_view(), name='user-update'),
]
