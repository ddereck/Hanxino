from django.urls import path

from admin_site.views import *
from .views import *
from .api import PaymentListCreateAPIView


urlpatterns = [
    path('', home, name='home'),
    path('discography/', discography, name='discography'),
    path('tours/', tours, name='tours'),
    path('join/', join, name='join'),
    path('videos/', videos, name='videos'),
    path('about/', about, name='about'),
    path('univers/', univers, name='univers'),
    path('api/kkiapay/callback/', kkiapay_callback, name='kkiapay_callback'),
    path('success/', success_view, name='success'),
    path('administration', administration, name='administration'),
    path('login', login, name = 'login'),
    path('api/admin-user-create/', AdminUserCreateAPIView.as_view(), name='admin-user-create'),
    path('api/reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('api/confirm-reset-password/', ConfirmResetPasswordAPIView.as_view(), name='confirm_reset_password'),
    path('api/payments/', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    
]
 