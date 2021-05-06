from django.shortcuts import render
from django.views.generic import View, ListView, FormView, DetailView
from visit.models import Visit
from visit.forms import VisitForm
from django.urls import reverse_lazy


class VisitListView(ListView):

    model = Visit
    template_name = 'index.html'


class AddUserView(FormView):

    form_class = VisitForm
    template_name = 'add_user_input.html'
    success_url = reverse_lazy('user-list')
    def form_valid(self, form):
        form.save()
        response = super().form_valid(form)
        return response

class DeliteUserView(View):

    def post(self, request , id):
        user = Visit.objects.get(pk=id)

        context = {"id": id, "user": user.user, "email": user.email, }
        user.delete()
        return render(
            template_name="delit_user.html",
            request=request,
            context=context
        )


class EdidUserView(View):

    def post(self, request, id):
        user = Visit.objects.get(pk=id)

        content = {"user": user.user, "email": user.email, "id": id}
        return render(
            template_name="eddit_user.html",
            context=content,
            request=request,
        )


def updated(request, id):

    user = Visit.objects.get(pk=id)
    user.user = request.POST.get("user")
    user.email = request.POST.get("email")

    user.save()

    context = {"id": id, "user": user.user, "email": user.email, }

    return render(
        template_name="add_user.html",
        request=request,
        context=context
    )