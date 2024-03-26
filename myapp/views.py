from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from .models import Announcement
from .forms import AnnouncementCreateForm


class AnnouncementListView(ListView):
    """Представление ленты объявлений"""
    model = Announcement
    template_name = 'announcements_list.html'
    context_object_name = 'announcements'


class AnnouncementDetailView(DetailView):
    """Представление объявления"""
    model = Announcement
    template_name = 'announcement_detail.html'
    context_object_name = 'announcement'


class AnnouncementCreateView(CreateView):
    """Представление создания объявления"""
    template_name = 'announcement_create.html'
    form_class = AnnouncementCreateForm
    model = Announcement

    # Добавление поля пользователя в форму
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnnouncementUpdateView(UpdateView):
    """Представление изменения объявления"""
    template_name = 'announcement_create.html'
    form_class = AnnouncementCreateForm
    model = Announcement


class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = 'announcement_delete.html'

    def get_success_url(self):
        return reverse('announce_list')


class PrivatePageView(TemplateView):
    """Представление приватной страницы каждого зарегистрированного пользователя"""
    template_name = 'private_page.html'

