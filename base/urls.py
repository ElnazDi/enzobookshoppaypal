from django.urls import path
from . import views


urlpatterns = [
    path('', views.store, name="store"),
    path('simple-checkout/', views.simpleCheckout, name="simple-checkout"),
    path('checkout/<int:pk>/', views.checkout, name="checkout"),
    path('complete/', views.paymentComplete, name="complete")
]
