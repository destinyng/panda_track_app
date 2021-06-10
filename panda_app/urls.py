
from django.urls import path
from . import views

#Post = redirect, get = render
urlpatterns = [
    path('', views.index), #same as localhost:8000/
    path('pandas/new', views.new_panda_page), #get, renders new.html
    path('pandas/create', views.create_panda), #post, make a new panda object
    path('pandas/<int:panda_id>', views.panda_profile), # same as localhost:8000/pandas/2
    path('pandas/<int:panda_id>/edit', views.edit_page), #get, renders the edit page
    path('pandas/<int:panda_id>/update', views.update) #post update the paanda
]
