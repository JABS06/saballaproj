from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name="Home"),
    path('Howtobuild/',views.Howtobuild, name="Howtobuild"),
    path('Builds/',views.Builds, name="Builds"),
    path('Mybuild/',views.Mybuild, name="Mybuild"),
    path('Tips/',views.Tips, name="Tips"),
    path('Createinfo/',views.Createinfo, name="Createinfo"),
    path('Profilelist/',views.Profilelist, name="Profilelist"),
    path('Componentlist/',views.Componentlist, name="Componentlist"),
    path('Service/<int:id>/',views.Service, name="Service"),
    path('Videos/',views.Videos, name="Videos"),
    path('About/',views.About, name="About"),
    path('Contact/',views.Contact, name="Contact"),
    path('Delbuild/<int:id>/',views.Delbuild, name = "Delbuild"),
    path('Delinfo/<int:id>/',views.Delinfo, name = "Delinfo"),
    path('Updateinfo/<int:id>/',views.Updateinfo, name = "Updateinfo"),
    path('Editinfo/<int:id>/',views.Editinfo, name = "Editinfo"),
    path('Feedbacks/',views.Feedbacks, name = "Feedbacks"),
    path('Feedbackdelete/<int:id>/',views.Feedbackdelete, name = "Feedbackdelete"),

]