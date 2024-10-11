from django.contrib import admin
from django.urls import path,include
from parkingapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [


    # path('', auth_views.LoginView.as_view(template_name='adminlogin.html'), name='adminlogin'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
    path('',views.adminlogin,name="adminlogin"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addvehicleentry/',views.addvehicle,name="addvehicleentry"),
    # path('category/',views.category,name="category"),
    path('logout/',views.logout_view, name='logout'),
    path('category/',views.add_category, name='add_category'),
    path('category/',views.category_list, name='category_list'),
    path('search/',views.search_vehicle, name='search_vehicle'),
    path('account/', views.account_settings, name='account_settings'),
]