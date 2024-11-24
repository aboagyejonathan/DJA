from django.contrib.auth import login
from custom_user.admin import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from verify_email.email_handler import ActivationMailManager

inactive_user = ''

def send_welcome_email(request):
        subject = 'Welcome To My Site'
        massage = 'Thank you for creating an account!'
        from_mail = 'admin@Mysite.com'
        global inactive_user
        recepient_list = [inactive_user]
        send_mail(subject,massage,from_mail,recepient_list)
        return redirect("Home")



# Create your views here.
class CustomLoginView(LoginView):
    template_name = "authentication/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
            return reverse_lazy("Home")

class CustomRegisterView(FormView):
    template_name = "authentication/registration.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("Home") # Automatically redirect to homepage after Registration


    def form_valid(self, form):
            # user = form.save()  # Automatically Save Registering User
            global inactive_user
            inactive_user = ActivationMailManager.send_verification_link(self.request, form)
            form.cleaned_data['email']
            if inactive_user is not None:
                login(self.request, inactive_user)  # Automatically log us in
            return super(CustomRegisterView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("Home")  # Prevent User Registration form from showing
        return super(CustomRegisterView, self).get(request, *args, **kwargs)
