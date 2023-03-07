from django.urls import include, path

from . import views

urlpatterns = [
    path('savedlocations', views.SavedLocationApiView),
    path('login', views.login_view),
    path('session', views.session_view),
    path('whoami', views.whoami_view),
    path('csrf', views.get_csrf),
]