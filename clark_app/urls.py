from django.urls import path

from clark_app.views.main import MainPageView, AuthPageView, RegisterPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('auth/', AuthPageView.as_view(), name='auth'),
    path('register/', RegisterPageView.as_view(), name='register')
]
