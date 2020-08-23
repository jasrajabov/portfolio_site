from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import blog.views

urlpatterns = [

    path('', blog.views.showAllBlogs, name='showAllBlogs'),
    path('<int:blog_id>/', blog.views.detail, name='detail' )
    ]
