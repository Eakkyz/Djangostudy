from django.urls import path
from myapp import views

urlpatterns = [
        #ใช้ฟังก์ชั้น index ใน views
        path('',views.index),
        path('about',views.about),
        path('form',views.form),
        path('edit/<person_id>',views.edit),
        path('delete/<person_id>',views.delete)

]
