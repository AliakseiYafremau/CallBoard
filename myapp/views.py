from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin

from .models import Announcement, Comment, User
from .forms import AnnouncementCreateForm, CommentForm


class AnnouncementListView(ListView):
    """Представление ленты объявлений"""
    model = Announcement
    template_name = 'announcements_list.html'
    context_object_name = 'announcements'


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.announcement_id = self.kwargs['pk']
        comment.save()
        return super().form_valid(form)


class AnnouncementDetailView(CommentCreateView, DetailView):
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


class ConfirmUserView(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'invalid_code.html')
        return redirect('account_login')