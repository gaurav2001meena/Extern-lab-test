from django.urls import path
from notes import views
from notes.controllers.register import register
from notes.controllers.login import login
from notes.controllers.create_document import create_document
from notes.controllers.delete_document import delete_document
from notes.controllers.show_all_doc import show_all_doc
from notes.controllers.doc_by_title import doc_by_title
from notes.controllers.update_document import update_document
urlpatterns = [
    path('' , views.index , name="index" ),
    path('register' , register , name='register'),
    path('login' , login , name='login'),
    path('create_document' , create_document , name="create_document"),
    path('delete_document' , delete_document, name="delete_document"  ),
    path('show_all_doc' , show_all_doc , name='show_all_doc'),
    path('doc_by_title' , doc_by_title , name='doc_by_title'),
    path('update_document', update_document, name='update_document')
]