from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePage, name='homePAGE'),
    path("shopPage/", views.shopPage, name='ShopHome'),
    path("about/", views.about, name='AboutUs'),
    path("contact/", views.contact, name='ContactUs'),
    path("tracker/", views.tracker, name='TrackingStatus'),
    path("products/", views.productView, name="ProductView"),
    path("search/", views.search, name='Search'),
    path("checkout/", views.checkout, name='Checkout'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('error2/', views.error2, name='error2'),
    path('error/', views.error, name='error'),
    path("logoutt/", views.Logout, name='logoutt'),
    path("logout/", views.LogoUt, name='LogOut')

]