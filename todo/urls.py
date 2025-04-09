from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/',views.signup),
    path('login/',views.Login),
    path('todo/',views.TodoPage),
    path('update_todo/<int:srno>/',views.Update,name = 'update_todo' ),
    path('delete_todo/<int:srno>/',views.Delete,name = 'delete_todo' ),
    path('signout/',views.Signout,name='signout'),

]

