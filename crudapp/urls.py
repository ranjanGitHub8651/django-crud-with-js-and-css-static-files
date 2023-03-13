from django.urls import include, path

from . import views

# from .views import MyView

# urlpatterns = [
#     path('', MyView.as_view()),
#     path('addnew/', MyView.as_view()),
# ]

urlpatterns = [
    path('', views.getEmployee),
    path('newemployee/', views.newEmployee),
    path('updateemployee/<int:id>/', views.updateEmployee),
    path('deleteemployee/<int:id>/', views.deleteEmployee),
]