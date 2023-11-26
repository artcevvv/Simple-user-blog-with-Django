# Simple user blog with Tinymce

Built with Django, Tinymce & [Bulma](https://bulma.io/)

Font: [Red Hat Mono SemiBold 600](https://fonts.google.com/specimen/Red+Hat+Mono)

Backend was made by Django. JS almost wasn't used(only tinymce ready JavaScript).

## Dependencies

>[!IMPORTANT]
>You need to create virtual enviroment using `python -m venv /path/to/new/virtual/environment`. 

>Moreover, you need to install django with `python -m pip install Django` and django-tinymce `pip install django-tinymce`

>For loading images install Pillow with `pip install pillow`

## Building

1. ### Run Migrations:
   Run `python manage.py makemigrations` followed by `python manage.py migrate` to create and apply the migrations to the database.
2. ### Create a Superuser:
   Use `python manage.py createsuperuser` to create a superuser account. This account will have access to the Django admin interface.
3. ### Access the Admin Interface:
   Start your Django development server using `python manage.py runserver` and navigate to [admin page](http://127.0.0.1:8000/admin/) in your browser. Log in using the superuser credentials created earlier.


## File structure

HTML files placed in [templates/blog](myblog/blog/templates/blog) folder. 

CSS file(main.css) placed in [myblog/static/css](myblog/static/css) folder.
