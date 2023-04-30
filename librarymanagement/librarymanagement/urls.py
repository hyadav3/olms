
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),

    path('adminclick', views.adminclick_view),


    path('adminsignup', views.adminsignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),

    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view),

    path('addbook', views.addbook_view),
    path('viewbook/', views.viewbook_view, name='view_book'),
    path('editbook/<int:book_id>/', views.edit_book_view, name='edit_book'),
    path('deletebook/<int:book_id>/', views.delete_book_view, name='delete_book'),

    path('aboutus', views.aboutus_view),
    

]
