from . import views
from django.urls import path , re_path


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('sum/', views.sum , name='sum'),


    path('parameter_path/<int:user_id>/', views.parameter_path , name='parameter_path'),
    path('parameter_pathh/<str:user_name>/<int:user_ids>/',views.parameter_pathh,name='parameter_pathh'),
    
    

    # using re_path(Regex Path)
# used for expressions complex patterns when need string,symbol,numbers

    # only numbers
    re_path(r'^re_path/(?P<year>[0-9]{4})/$',views.re_path,name="re_path"),

    # for numbers,symbol etc
    re_path(r'^re_path1/(?P<bro_id>[a-zA-Z0-9_!@\-]+)/$',views.re_path1, name="re_path2"),






    # using **kwargs

     # for numbers,symbol etc
    path('kwargs/<str:username>/<int:age>/',views.details,name="Kwargs"),

    # if one argument is missing

    path('fullinfo/<str:username>/<int:age>/',views.detailss,name="username"),

    # ONLY username (age will be missing)
    path('fullinfo/<str:username>/', views.detailss),
]







    