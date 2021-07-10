from django.urls import path
from . import views
app_name = 'todo_app'
urlpatterns = [
    path('', views.funtask, name='funtask'),
    path('add', views.addtask, name='addtask'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('taskview', views.taskListView.as_view(), name='taskview'),
    path('detailview/<int:pk>', views.detailview.as_view(), name='detailview'),
    path('updateview/<int:pk>', views.updateview.as_view(), name='updateview'),
    path('deleteview/<int:pk>', views.deleteview.as_view(), name='deleteview'),
]