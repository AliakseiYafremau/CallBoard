from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .filters import CommentFilter
from .models import Announcement, Comment, User
from .forms import AnnouncementCreateForm, CommentForm


class AnnouncementListView(ListView):
    """Представление ленты объявлений"""
    model = Announcement
    template_name = 'announcements_list.html'
    context_object_name = 'announcements'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['is_authenticated'] = self.request.user.is_authenticated
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
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


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    """Представление создания объявления"""
    template_name = 'announcement_create.html'
    form_class = AnnouncementCreateForm
    model = Announcement

    # Добавление поля пользователя в форму
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnnouncementUpdateView(LoginRequiredMixin, UpdateView):
    """Представление изменения объявления"""
    template_name = 'announcement_create.html'
    form_class = AnnouncementCreateForm
    model = Announcement



#class AnnouncementDeleteView(DeleteView):
#    model = Announcement
#    template_name = 'announcement_delete.html'
#
#    def get_success_url(self):
#        return reverse('announce_list')


class PrivatePageView(LoginRequiredMixin, ListView):
    """Представление приватной страницы каждого зарегистрированного пользователя"""
    model = Comment
    template_name = 'private_page.html'
    context_object_name = 'comments'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CommentFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


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


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        return reverse('private_page')
