from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import (
    index,
    about_us,
    contact_us,
    author,
    presentation,
)

urlpatterns = [
    path("", index, name="index"),
    path('about-us/', about_us, name='about-us'),
    path('contact-us/', contact_us, name='contact-us'),
    path('author/', author, name='author'),
    # Authentication
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name='password_change_done'),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/',
         views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Sections
    path('presentation/', presentation, name='presentation'),
    path('page-header/', views.page_header, name='page_header'),
    path('features/', views.features, name='features'),
    path('navbars/', views.navbars, name='navbars'),
    path('nav-tabs/', views.nav_tabs, name='nav_tabs'),
    path('pagination/', views.pagination, name='pagination'),
    path('inputs/', views.inputs, name='inputs'),
    path('forms/', views.forms, name='forms'),
    path('alerts/', views.alerts, name='alerts'),
    path('modals/', views.modals, name='modals'),
    path('tooltips/', views.tooltips, name='tooltips'),
    path('avatars/', views.avatars, name='avatars'),
    path('badges/', views.badges, name='badges'),
    path('breadcrumbs/', views.breadcrumbs, name='breadcrumbs'),
    path('buttons/', views.buttons, name='buttons'),
    path('dropdowns/', views.dropdowns, name='dropdowns'),
    path('progress-bars/', views.progress_bars, name='progress_bars'),
    path('toggles/', views.toggles, name='toggles'),
    path('typography/', views.typography, name='typography'),

]

app_name = "taxi"
