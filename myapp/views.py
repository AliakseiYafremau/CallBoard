from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin

from .models import Announcement
from .forms import AnnouncementCreateForm, CommentForm


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = CommentForm
        return context_data

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        print(text)
        return reverse('announce_detail', args=[kwargs.get('pk')])

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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

