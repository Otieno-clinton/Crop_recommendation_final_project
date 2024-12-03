from django.contrib import admin
from django.urls import path
from recommendapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.index, name="home"),
    path("", views.landing, name="landing"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),

    path("testimonials/", views.testimonials, name="testimonials"),
    path("blogdetails/", views.blogdetails, name="blogdetails"),
    path("contactinfo/<int:id>/", views.contactinfo, name="contactinfo"),

    path('register/farmer/', views.farmer_register, name='farmer_register'),
    path('register/gov/', views.gov_register, name='gov_register'),
    path('register/ngo/', views.ngo_register, name='ngo_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgotpassword/', views.forgot_password, name='forgotpassword'),
    path('recommend/', views.recommend, name='recommend'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
