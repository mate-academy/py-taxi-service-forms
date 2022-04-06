# Taxi service home page

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In this task, you should implement the home page of the site.

1. Inside `taxi_service.urls` add path to the `taxi.urls`. Use
function [include()](https://docs.djangoproject.com/en/4.0/ref/urls/#django.urls.include).
2. Inside `taxi.urls` create a path for the home page. This
page should open when you are accessing `http://127.0.0.1:8000/`. Give this
path the name `index`, import `index` function from `taxi.views`, assign this
function as a handler of this path, you will implement this function soon.
Also, add `app_name` with appropriate value.
3. Inside `taxi.views` create function `index`. "Views" functions always 
take the parameter `request`. In this function:
    - count the number of all drivers
    - count the number of all manufacturers
    - count the number of all cars
    - save these numbers in variable context with appropriate keys, later you
will use these keys in the template
    - return `HttpResponse` with rendered template combined with context. Use 
[render()](https://docs.djangoproject.com/en/4.0/topics/http/shortcuts/#render). 
Pass there `request`, the path to the template `"taxi/index.html"` (you will create
template soon), context with numbers.
4. Before you create a template you have to create styles for the 
template. Create directory `static` next to directory `taxi`. Inside this 
directory create a file with the following path `css/styles.css`. Don't forget to
add roots to the settings (`STATICFILES_DIRS` and `STATIC_ROOT`). Also, you 
need to serve static files during the development, use 
[static()](https://docs.djangoproject.com/en/4.0/howto/static-files/#serving-static-files-during-development)
and add path to the `urlpatterns`.
5. Create directory `templates` next to the directory `taxi`. There you will
store templates for pages. Edit `TEMPLATES` inside settings, set the appropriate 
value for the key `DIRS`, `DIRS` defines a list of directories where the engine 
should look for template source files.
6. Inside directory `templates` create template `base.html`, it is a parent 
template, other templates will extend `base.html`. Inside `base.html`:
   - Inside `<head>`:
      - Create block `title` with `Taxi Service` title inside
      - Load static and import `styles.css` via `<link rel...>`
   - Inside `<body>`:
      - Create block `sidebar`
      - Create block `content`
      - Create block `pagination`
7. Inside `templates` create a directory `taxi`. There you will store templates
for the app `taxi`. Create `index.html` there. Inside `index.html`:
    - Extend from `base.html`
    - Override block `content` and place information about:
        - Number of cars
        - Number of drivers
        - Number of manufacturers
      
      as a list.
8. Create some drivers, manufacturers, and cars. Run server, open 
`http://127.0.0.1:8000/`, check if the information is there and if it is 
correct.
