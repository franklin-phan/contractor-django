from django.shortcuts import render
from django.urls import path
from items.views import ItemListView, ItemDetailView, ItemNew, ItemUpdate, delete_object


urlpatterns = [
    path('', ItemListView.as_view(), name='item-list-page'),
    path('submit/', ItemNew.as_view(), name="submit-item"),
    path('<str:slug>/update', ItemUpdate.as_view(), name='item-update-page'),
    path('<str:slug>/delete', delete_object, name='item-delete-page'),
    path('<str:slug>/', ItemDetailView.as_view(), name='item-details-page'),
    
]