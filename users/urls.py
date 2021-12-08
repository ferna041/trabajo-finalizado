from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/<slug:slug>', views.user_detail, name='user_detail'),
    path("follow/<slug:slug>", views.follow, name='follow'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path("followers/", views.followers_view, name="followers"),
    path("following/", views.following_view, name="following"),
    path("followers_user/", views.followers_user_view, name="followers_user"),
    path("following_user/", views.following_user_view, name="following_user"),
    path("Posts",views.post_profile, name="post_profile"),
    path("posts",views.post_user, name="post_user"),
]

