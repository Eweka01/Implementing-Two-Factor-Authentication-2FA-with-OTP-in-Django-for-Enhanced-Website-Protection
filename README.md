# Implementing Two-Factor Authentication 2FA with OTP in Django for Enhanced-Website-Protection

# Django OTP Integration Task

This README provides an overview of the task steps followed to integrate OTP (One-Time Password) authentication into a Django project.

## Steps:

1. **Install Django and Create Project**
    - Installed Django and set up a virtual environment.
    - Initialized a new Django project.

2. **Install Django OTP**
    - Installed `django-otp` package for enabling two-factor authentication.
    - Updated `settings.py` to include `django_otp` and `otp_totp` in the `INSTALLED_APPS`.

3. **Configure URLs**
    - Updated `urls.py` to replace the default Django admin with `OTPAdminSite` to enable OTP for admin logins.

4. **Database Migrations**
    - Applied migrations to set up necessary database tables using `python3 manage.py migrate`.

5. **Create Superuser**
    - Created a superuser account using `python3 manage.py createsuperuser`.

6. **OTP Token Login**
    - Accessed the Django admin login page, configured an OTP device, and verified that OTP-based login works as expected.

## Final Outcome:
The Django admin panel now requires OTP in addition to the username and password for logging in, securing the admin interface with two-factor authentication.

---
