# Simple user blog with Django & Tinymce 



## Tech Stack

Made with Django(supports 4.2.7), Tinymce & [Bulma](https://bulma.io/)

Font: [Red Hat Mono SemiBold 600](https://fonts.google.com/specimen/Red+Hat+Mono)

Back-end was made by Django. JS wasn't used (only Tinymce JavaScript).

## Dependencies

>[!IMPORTANT]
>1. Create virtual enviroment using `python -m venv /path/to/new/virtual/environment`. 
>
>2. Install django with `python -m pip install Django` and django-tinymce `pip install django-tinymce` 
>
>3. For loading images install Pillow with `pip install pillow` 

## Building

1. ### Run Migrations:
   Run `python manage.py makemigrations` followed by `python manage.py migrate` to create and apply the migrations to the database.
2. ### Create a Superuser:
   Use `python manage.py createsuperuser` to create a superuser account. This account will have access to the Django admin interface.
3. ### Access the Admin Interface:
   Start your Django development server using `python manage.py runserver` and navigate to [admin page](http://127.0.0.1:8000/admin/) in your browser. Log in using the superuser credentials created earlier.


## File structure

HTML placed in [templates/blog](myblog/blog/templates/blog).

CSS placed in [myblog/static/css](myblog/static/css).
