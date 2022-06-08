from django.urls import path
from backend import views
from django.contrib.auth import views as auth_views

app_name = 'backend'

urlpatterns=[
  # path('login/', views.login, name='login'),
  path('backendblog/', views.backendblog, name='backblog'),
  path('viewblog/', views.view_blog, name='viewblog'),
  path('edit_profile/', views.edit_profile, name='edit_profile'),
  path('view_profile/', views.view_profile, name='view_profile'),
  path('base/', views.base, name='base'),
  path('changepassword/', views.passwordview, name='changepassword'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('addblog/', views.add_blog, name='addblog'),
  path('editpost/<int:pk>', views.edit_post, name='editpost'),
  path('viewpost/<int:pk>', views.view_post, name='viewpost'),
  path('delete/<int:pk>', views.delete_post, name='deletepost'),
  path('logout_page/', views.signout, name='logout_view'),
  path('login/',auth_views.LoginView.as_view(template_name='backend/login.html'), name='login'),
  
  # path('logout-page/',auth_views.LogoutView.as_view(template_name='back_end/logout.html'),name='logout'),
  # path('confirm_logout/',views.confirm_logout, name='confirm_logout'),
  
]