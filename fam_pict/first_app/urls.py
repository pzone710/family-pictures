from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('signup/', views.form_request, name='signup')
]
