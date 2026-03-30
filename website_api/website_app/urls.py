from django.contrib import admin
from django.urls import path
from website_app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
     path('',views.home, name='home'),
     path("Property",views.PropertyAdd, name='Property'),
     path("Architect",views.Architect, name='Architect'),
     path("Soil_Firms",views.Soil_Firms, name='Soil_Firms'),
     path("Solar_Firms",views.Solar_Firms, name='Solar_Firms'),
     path("Vetting_Engineers",views.Vetting_Engineers, name='Vetting_Engineers'),
     path("Register",views.Registerform, name='Register'),
     path("Contact",views.Contactform, name='Contact'),
     path("Categories",views.Category_registrationform, name='Category_registration'),
     path("View_property",views.View_property, name='View_property'),
     path("Update_form/<int:reg_no>", views.Updateform, name='Updateform'),
     path("Deleterecord/<int:reg_no>",views.DeleteRecord, name='delete'),
     path("Update_property/<str:agency>", views.Update_property, name='Update_property'),
     path("Delete_property/<str:agency>",views. Delete_property, name='Delete_property'),
     path("Login_page",views.Login_page, name='Login'),
     path("Signup_page",views.Signup_page, name='Signup'),
     path("Logout_page",views.Logout_page, name='Logout'),
     
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

