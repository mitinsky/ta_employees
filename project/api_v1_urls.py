from django.urls import include, path


urlpatterns = [
    path('employees/', include('apps.employees.urls')),
]
