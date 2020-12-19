from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    # path('extract_report', login_required(views.ExtractReport.as_view()), name='extract_report'),
]
