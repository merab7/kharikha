from django.urls import path
from .views import cart_sum, cart_add, cart_del, edit, update, cupon_code


urlpatterns = [
    path('sum/', cart_sum, name='cart_sum' ),
    path('add/',cart_add, name='cart_add'),
    path('edit/<int:id>/<size>/',edit, name='edit'),
    path('delete/<int:id>/<size>/', cart_del, name='cart_del'),
    path('update/', update, name='update'),
    path('cupon_code/', cupon_code, name='cupon_code'),
]