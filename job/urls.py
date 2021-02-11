from django.urls.conf import path
from .import views

urlpatterns = [
    path("",views.job_list,name="job_list"),
    path("add/",views.job_post,name="job_post"),
    path("<str:slug>",views.job_detail,name="job_detail"),
]
