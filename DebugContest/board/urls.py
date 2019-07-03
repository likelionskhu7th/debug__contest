from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #board.html
    path('board/',views.board,name="board"),
    #create.html
    path('create/',views.create,name="create"),
    path('createblog/',views.boardform, name='createblog'),
    #edit.html
    path('<int:pk>/edit/',views.edit,name='edit'),
    path('<int:pk>/remove/',views.remove,name="remove"),
    #hashtag
    path('hashtag/',views.hashtagform,name="hashtag"),
    #detail.html
    path('<int:pk>', views.detail, name='detail'),
    path('<int:pk>/comment_remove',views.comment_remove ,name="comment_remove"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

