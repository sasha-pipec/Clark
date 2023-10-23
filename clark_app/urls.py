from django.urls import path

from clark_app.views.main import MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main')
]
