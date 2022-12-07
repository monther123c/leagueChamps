from django.urls import path
from .views import champListView,champDetailView,champCreateView,champUpdateView,champDeleteView 

urlpatterns=[
    path('champ/',champListView.as_view(),name='champ_list'),
    path('champ/<int:pk>/',champDetailView.as_view(),name='champ_detail'),
    path('champ/create/',champCreateView.as_view(),name="champ_create"),
    path ('champ/<int:pk>/update/',champUpdateView.as_view(),name='champ_update'),
    path('champ/<int:pk>/delete/',champDeleteView.as_view(),name='champ_delete')
]