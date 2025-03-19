from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
from .models import Course, Review
from django.contrib.auth.models import User, auth
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm, ReviewForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['reviews'] = Review.objects.all()
        return context

class CoursesView(ListView):
    model = Course
    template_name = 'course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')  # Replace with your actual success URL

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        if User.objects.filter(username=username).exists():
            messages.error(self.request, 'Username Already Exists!')
            return self.form_invalid(form)
        elif User.objects.filter(email=email).exists():
            messages.error('Email Already In Use!')
            return self.form_invalid(form)
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')  # Replace with your actual success URL

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Invalid Credentials!')
            return self.form_invalid(form)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'submit_review.html'
    success_url = reverse_lazy('index')

    # LoginRequiredMixin settings
    login_url = 'login'  # Redirects unauthenticated users to this URL

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Add a message before redirecting to the login page
            messages.error(request, "You need to log in to submit a review.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Check if the user has already submitted a review
        existing_review = Review.objects.filter(user=self.request.user).first()
        if existing_review:
            # Add an error message and redirect if the user already has a review
            messages.error(self.request, "You have already submitted a review!")
            return redirect(self.success_url)

        # Associate the review with the logged-in user before saving
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewView(ListView):
    model = Review
    template_name = 'all_reviews.html'
    context_object_name = 'reviews'

class AboutUsView(TemplateView):
    template_name = 'about_us.html'