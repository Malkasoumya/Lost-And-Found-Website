
from django.contrib import admin
from django.urls import path,include

from pages.views import home_view,lost_view,found_view,about_view
from lost.views import lost_view
from lost.views import lost_enter
from lost.views import found_enter
from lost.views import found_view
from lost.views import available_items
from users.views import register,profile
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users.views import lost,logout_view
from users.views import found
from users.views import updateProfile
from users.views import post_delete_view,post_delete_view1
from users.views import specific_post_view,specific_post_view1,activelost,activefound
from users.views import reset_password
from users.views import forgot_password
from users.views import custom_login,verify_otp

urlpatterns = [
    path('profile/update/',updateProfile,name='update'),
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    #path('home/',home_after_login_view,name='home_after_login'),
    path('reportLost/',lost_enter,name='enter_lost'),
    path('lostlist/',lost_view,name='lost_list'),
    path('foundList/',found_view,name='found_list'),
    path('reportFound/',found_enter,name='enter_found'),
    path('about/',about_view,name='about_us'),
    #login
    path('login/', custom_login, name='login'),
    path('available_items/', available_items, name='available_items'),
    #register
    #path('register/',register,name='register'),
    #path('adduser/',addUser,name='addUser'),
    path('forgot_password',forgot_password,name='forgot_password'),
    #register
    path('register/',register,name='register'),
    path('reset_password/',reset_password,name='reset_password'),
    path('verify_otp/' ,verify_otp,name='verify_otp'),
    #login
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout_view/',logout_view,name='logout_view'),
    path('profile/',profile,name='profile'),
    path('profile/my_found_things/',found,name='found_specific'),
    path('profile/my_lost_things/',lost,name='lost_specific'),
    path('profile/my_found_things/active/<int:id>/delete/',post_delete_view,name='product-delete-f'),
    path('profile/my_lost_things/active/<int:id>/delete/',post_delete_view1,name='product-delete-l'),
    path('profile/my_found_things/active/<int:id>/',specific_post_view,name='specific-post-view-f'),
    path('profile/my_lost_things/active/<int:id>/',specific_post_view1,name='specific-post-view-l'),
    path('profile/my_lost_things/active/',activelost,name='lost_specific_active'),
    path('profile/my_found_things/active/',activefound,name='found_specific_active'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)