from django.urls import path
from .views import Home, CoursesView, CourseDetailView, RegisterView, LoginView, ReviewCreateView, ReviewView, AboutUsView

#Url patters for the app

urlpatterns = [path('', Home.as_view(), name='index'), path('courses', CoursesView.as_view(), name='courses'), path('course-detail/<int:pk>', CourseDetailView.as_view(), name='course_detail'), path('register', RegisterView.as_view(), name='register'), path('login', LoginView.as_view(), name='login'), path('submit-review', ReviewCreateView.as_view(), name='submit_review'), path('reviews', ReviewView.as_view(), name='reviews'), path('about-us', AboutUsView.as_view(), name='about_us')]
