from django.urls import path, re_path

from .views import ListCategories, CategoryDetailView

urlpatterns = [
    re_path(r'^category/$', ListCategories.as_view()),
    re_path(r'^category/(?P<pk>[0-9]+)/$', CategoryDetailView.as_view())
]