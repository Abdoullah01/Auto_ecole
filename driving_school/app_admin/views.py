from django.shortcuts import render, redirect
from schoolDrive.models import Personne
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from schoolDrive.forms import PersonneForm



# Create your views here.
def dashboard(request):
    return render(request, 'app_admin/db.html')

login_required
def user_articles(request):
    has_perm = False
    if request.user.has_perm("blog.delete_article"):
        has_perm = True
    list_articles = Personne.objects.filter(user = request.user)
    return render(request, 'app_admin/my-articles.html', {'list_articles':list_articles, "has_perm":has_perm})

class AddArticle(LoginRequiredMixin,CreateView):
    model = Personne
    form_class = PersonneForm
    template_name = "app_admin/add-article.html"
    success_url = "my-articles"
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateArticle(LoginRequiredMixin,UpdateView):
    model = Personne
    form_class = PersonneForm
    template_name = 'app_admin/article_form.html'
    
    
    
class DeleteArticle(DeleteView):
    model = Personne
    success_url = "/app-admin/my-articles"

def dispatch(self, request, *args, **kwargs):
    if not request.user.has_perm("blog.delete_article"):
        raise PermissionDenied
    return super().dispatch(request, *args, **kwargs)
