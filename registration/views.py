from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.core.tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.encoding import force_byte
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit = False)
            user.is_active = False
            user.save()
            curreent_site = get_current_site(request)
            subject = 'Activate your swagg Store Account'
            message = render_to_string('registration/acct_activate.html'),{
                'user': user,
                'domain': current_site.domain,
                'uid':  urlsafe_base64_encode(force_byte(user.pk)),
                'token': account_activation_token.make_token(user),
            } 
            user.email_user(subject, message)
            return redirect('account_activation_sent')
        else:
            signup_form = SignUpForm()
        return render(request 'registration/signup.html', {'signup_form': signup_form})

