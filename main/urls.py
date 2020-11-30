
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("login", views.login),
    path("success", views.success),
    path("form",views.form),
    path("post",views.post),
    path("post_comment",views.post_comment),
    path("delete/<int:post_id>",views.delete),
    path("logout", views.logout)
]
