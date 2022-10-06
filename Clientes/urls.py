from django.urls import path 

from . import views

urlpatterns = [
   path('',views.index, name='inicio' ),
   path('blank/',views.vacio, name='blank' ),
   
    ] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



