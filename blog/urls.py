from django.contrib import admin
from django.urls import path
from .views import *   

urlpatterns = [    # include한 path url의 이름이 url 앞에 붙음. (app 별로 url을 관리)
    path('<str:id>', detailHtml, name="detailHtml"),  # '<str=id>' 에서 id는 view 함수의 매개변수 이름으로 id 값에 따라 페이지가 다르게 보임. id가 views.py 함수에 매개변수로 들어감.
    path('new/', newHtml, name="newHtml"),
    path('create/', createPost, name="createPost"),
    path('edit/<str:id>',editHtml, name="editHtml"),  # path conveter로 받을 아이디를 수정하는 창을 보여줌. 
    path('update/<str:id>',upadatePost, name="updatePost"), # path conveter를 반드시 주어야지 views.py에 매개변수로 전달할 수 있음.
    path('delete/<str:id>', deletePost, name="deletePost"),  # path conveter 반드시 줘야함.
]