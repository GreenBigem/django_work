from django.urls import path
from . import views

urlpatterns = [

    # Рекламная часть сайта
    path('', views.index, name='index'),
    path('finance/', views.finance, name='finance'),
    path('finance/accounts/create', views.account_create),
    path('finance/operations/create', views.operation_create),
    path('finance/operations/delete/<int:id>', views.operation_delete, name='operation_delete')

]
