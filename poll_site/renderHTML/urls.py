from django.urls import path
from .views import *

urlpatterns = [
    path('', restaurant, name='Restaurant_Page'),
    path('dish/<int:restaurant_id>', dish, name='dish'),
    path('review/<int:dish_id>', review, name='review'),
    path('delete_restaurant/<int:restaurant_id>', delete_restaurant_data, name="delete_restaurant"),
    path('delete_dish/<int:pk>/<int:dish_id>', delete_dish_data, name="delete_dish"),
    path('delete_review/<int:pk>/<int:review_id>', delete_review_data, name="delete_review"),
    path('update_restaurant/<int:restaurant_id>', update_restaurant_data, name="update_restaurant"),
    path('update_dish/<int:pk>/<int:dish_id>', update_dish_data, name="update_dish"),
    path('update_review/<int:pk>/<int:dish_id>', update_review_data, name="update_review"),
    path('show/', show_data, name="show"),
    path('delete/<int:id>', delete_data, name="delete"),
    path('update/<int:id>', update_data, name="update"),
    path('renderHTML/', restaurant, name="add"),
    path('search/', search, name="search"),
    path('register/', register, name="register"),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
