from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
# from .views import signup, CustomLoginView

urlpatterns=[
    path("", views.index, name="index"),
    path('all-posts/', views.all_posts, name='all_posts'),
    path('add-post/', views.add_post, name='add_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('users_view/', views.view_user, name="view_user"),
    path('user_detail/<int:id>/', views.edit_user, name="edit_user"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('view-post/', views.show, name='show'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update, name='update'),
    path('test_ckeditor/', views.test_ckeditor, name='test_ckeditor'),
    path("delete_post/<int:id>", views.delete_post, name="delete_post"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='my_app/login.html'), name='login'),
    path('login_view/', views.login_view, name='login_view'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='my_app/logout.html'), name='logout'),
    path('accounts/profile/', views.user_dashboard, name='user_dashboard'),
    path('signup/', views.admin_signup, name='admin_signup'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('delete_user/<int:id>/', views.delete_users, name="delete_users"),
    path('settings/', views.settings, name="settings"),
    # path('admin/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='my_app/login.html'), name='login'),

    path('admin-logout/', views.admin_logout, name='logout'),
    path('logout/', views.user_logout, name='user_logout'),
    path ('test/', views.test, name='test'),
    path ('comments/', views.comments, name='comments'),
    path('edit-comment/<int:id>/', views.edit_comment, name='edit_comment'),
    path('update-comment/<int:id>/', views.update_comment, name='update_comment'),
    path('delete-comment/<int:id>/', views.delete_comment, name='delete_comment'),





]
