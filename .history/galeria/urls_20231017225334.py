from django.urls import path
from galeria.views import index

urlpatterns = [
    path('', admin.site.urls),
    path('', index),
]