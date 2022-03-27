# Taxi service class-based views

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In this task, you should implement class-based list and detail views.

1. Create manufacturer list view `ManufacturerListView`:
    - For the class-based list view use `ListView` from 
`django.views.generic`.
    - Access to this page should be prohibited for a non-logged-in user, 
use `LoginRequiredMixin` from django.contrib.auth.mixins. **Use this mixin for
all class-based views.** Always place mixins at the leftmost position in the 
inheritance list.
    - Set `model` - model on which the list view is built.
    - Set `context_object_name`in order to set the appropriate context variable 
name, that you will use in the template.
    - Set `queryset` - queryset that will be stored in `context_object_name`,
select all manufacturers, they should be ordered by `name` by default - add 
`ordering` on the model.
    - Set `template_name` - the name of the template, that view will use, it 
should be placed inside `templates/taxi`
    - Set `paginate_by` equals to 2. This variable indicates how many instances
should be displayed on a single page.

2. Create manufacturer creation view `ManufacturerCreateView`:
    - For the class-based create view use `CreateView` from 
`django.views.generic`.
    - Set `model`.
    - Set `fields`, means the list of fields that you want to fill while creating
the manufacturer. If you want all fields - set to `"__all__"`.
    - Set `success_url`, success_url is the URL to redirect to when the form 
is successfully processed. Use [reverse_lazy](https://docs.djangoproject.com/en/4.0/ref/urlresolvers/#reverse-lazy) 
here, you can pass there `path` looks like `app_name:url_path_name`, pass 
there `"taxi:manufacturer-list"`, later you will create that path.
    - Django will search template with the suffix `_form` for create and update
views by default. 
For example, for `model` `Manufacturer` Django will search 
`taxi/manufacturer_form.html` template, you will create this template soon.

3. Create manufacturer update view `ManufacturerUpdateView`:
    - For the class-based update view use `CreateView` from 
`django.views.generic`.
    - Just like in the CreateView, set appropriate `model`, pick all `fields` 
for the update, and after successful completion the form redirect to a path with 
name `manufacturer-list`

4. Create manufacturer delete view `ManufacturerDeleteView`:
    - For the class-based delete view use `DeleteView` from 
`django.views.generic`.
    - Set only `model` and `success_url`.

5. Create car list view `CarListView`:
    - Set `model`, `paginate_by`, `queryset`.
    - Note: Car model has foreign key `manufacturer`, to improve query 
performance use [select_related](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#select-related).

6. Create car detail view `CarDetailView`:
    - For the class-based detail view use `DetailView` from 
`django.views.generic`.
    - Set only `model`.

7. Create car delete view `CarDeleteView`:
    - Set `model` and `success_url`. After form successfully processed redirect 
to `car-list` path.
    
8. Create driver list view `DriverListView`:
    - Set `model` and `paginate_by`.

9. Create driver detail view `DriverDetailView`:
    - Set `model` and `queryset`.
    - In this view, you display information about cars of the driver. In order 
not to make a query for a manufacturer for each car use 
[prefetch_related](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#prefetch-related) 
for `cars__manufacturer`.

10. Create driver delete view `DriverDeleteView`:
    - Set `model` and `success_url`. After the form is successfully processed redirect 
to the `driver-list` path.

11. Inside `taxi/urls.py`:
    - Import all your created views.
    - To set the class-based view as a handler use method `as_view()`.
    - Create such paths:
      - By `manufacturers/` you should get manufacturer list view. Give these paths 
appropriate names, because some of them you already have used in `success_url` 
in views.
      -  `manufacturers/create/` - manufacturer create view.
      -  `manufacturers/pk/update/` - manufacturer create view.
`pk` is a number, primary key of manufacturer to update.
      -  `manufacturers/pk/delete/` - manufacturer delete view.
      -  `cars/` - car list view.
      -  `cars/pk/` - car detail view.
      -  `cars/pk/delete/` - car delete view.
      -  `drivers/` - driver list view.      
      -  `drivers/pk/` - driver detail view.
      -  `drivers/pk/delete/` - driver delete view.

12. Create templates for the views. By default, class-based views try to find      
a template based on the model name and certain suffix: 
    1. For list view - `-list`
    2. For detail view - `_detail`
    3. For update or create view - `_form`
    4. For delete view - `_confirm_delete`
    - Create templates for manufacturer list, car list, driver list. In these
templates:
        - Add a button with a link to create an instance page. (manufacturer, car, 
driver relatively)
        - Table with the information of each instance.
            1. In the manufacturer list there should be links for update and delete 
        pages of the manufacturer
            2. In the car list set a link on the id field that leads to the car 
        detail page. Set [get_absolute_url()](https://docs.djangoproject.com/en/4.0/ref/models/instances/#get-absolute-url)
        for models to have a link to the instance page in the admin 
        and use this method in templates 
            3. In the driver list set a link on the username field that leads to the  
        driver detail page 
    - Create driver detail template:
        - Add button for delete driver 
        - Place information about all cars of the driver
    - Create car detail template:
        - Add buttons for update and delete car 
        - Place information about the manufacturer of the car (name, country)
        - Place information about all drivers of that car.
    - Create manufacturer update and create templates:
        - Place the form 
    - Create manufacturer/car/driver delete view:
        - Ask the user if he sure
        - Place the form to confirm
    - Inside `templates` create directory `includes`, create `sidebar.html` 
    there. In this file place links to the home page, manufacturer list page,
    car list page, drivers list page.
    - In `base.html` include `sidebar.html` in block `sidebar`, so all these
    links will be accessible on all pages.
    