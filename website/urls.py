from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('post/', include(('post.urls', 'post'), namespace='post')),
    path('user/', include(('user.urls', 'user'), namespace='user'))
]
