from django.urls import path
from .views import AnnouncementListView, AnnouncementDetailView, PrivatePageView, AnnouncementCreateView, \
    AnnouncementUpdateView, AnnouncementDeleteView, CommentCreateView

urlpatterns = [
    path('', AnnouncementListView.as_view(), name='announce_list'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='announce_detail'),
    path('private_page/', PrivatePageView.as_view(), name='private_page'),
    path('announcement/create/', AnnouncementCreateView.as_view(), name='announce_create'),
    path('announcement/update/<int:pk>/', AnnouncementUpdateView.as_view(), name='announce_update'),
    path('announcement/delete/<int:pk>/', AnnouncementDeleteView.as_view(), name='announce_delete'),
    path('announcement/<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment_create')
]
