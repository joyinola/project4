
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('follow/<str:user>', views.Follow, name='follow'),
    path("posts", views.index, name="index"),
    path('following', views.following,name='following'),
    path('edit/<int:post_id>',views.edit,name='edit'),
    path('like/<int:post_id>',views.like, name='like'),
    path('profile/<str:user_profile>',views.Profile,name='Profile'),
    path('new',views.new_post, name='new_post'),
    path("",views.login_view, name="login"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
