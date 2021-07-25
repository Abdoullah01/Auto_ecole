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
def user_eleves(request):
    has_perm = False
    if request.user.has_perm("schoolDrive.delete_eleve"):
        has_perm = True
    list_eleves = Personne.objects.filter()
    return render(request, 'app_admin/eleve.html', {'list_eleves':list_eleves, "has_perm":has_perm})

class AddPersonne(LoginRequiredMixin,CreateView):
    model = Personne
    form_class = PersonneForm
    template_name = "app_admin/add-eleve.html"
    success_url = "eleve"
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateArticle(LoginRequiredMixin,UpdateView):
    model = Personne
    form_class = PersonneForm
    template_name = 'app_admin/eleve_form.html'
    
    
    
class DeleteArticle(DeleteView):
    model = Personne
    success_url = "/app-admin/eleve"

def dispatch(self, request, *args, **kwargs):
    if not request.user.has_perm("schoolDrive.delete_eleve"):
        raise PermissionDenied
    return super().dispatch(request, *args, **kwargs)
