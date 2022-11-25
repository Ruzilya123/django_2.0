
from django.urls import path, include
from . import views

post_patterns = [
    path('', views.posts, name='post'),
    path('popular', views.popular, name='popular posts'),
    path('last', views.last, name='last posts'),
    path('comments', views.comments, name='comments'),
    path('likes', views.likes, name='likes')
]

urlpatterns = [
    path('index/<int:id>', views.index, name='home'),
    path('posts/<int:id>/', include(post_patterns), name='posts'),
    path('user/', views.user, name='user'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('access/<str:login>/<str:password>/', views.access, name='access'),
    path('json/', views.json, name='json'),
    path('set/', views.set, name='set'),
    path('get/', views.get, name='get')
]

