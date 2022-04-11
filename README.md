# Taxi service class-based views

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In this task, you should implement class-based list and detail views.

1. Create manufacturer list view `ManufacturerListView`:
    - For the class-based list view use `ListView` from 
`django.views.generic`.
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
    
2. Create car list view `CarListView`:
    - Set `model`, `paginate_by`, `queryset`.
    - Note: Car model has foreign key `manufacturer`, to improve query 
performance use [select_related](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#select-related).

3. Create car detail view `CarDetailView`:
    - For the class-based detail view use `DetailView` from 
`django.views.generic`.
    - Set only `model`.
    
4. Create driver list view `DriverListView`:
    - Set `model` and `paginate_by`.

5. Create driver detail view `DriverDetailView`:
    - Set `model` and `queryset`.
    - In this view, you display information about cars of the driver. In order 
not to make a query for a manufacturer for each car use 
[prefetch_related](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#prefetch-related) 
for `cars__manufacturer`.

6. Inside `taxi/urls.py`:
   - Create such paths:
     - By `manufacturers/` you should get manufacturer list view.
     -  `cars/` - car list view.
     -  `cars/pk/` - car detail view.
     -  `drivers/` - driver list view.      
     -  `drivers/pk/` - driver detail view.

7. Create templates for the views. By default, class-based views try to find      
a template based on the model name and certain suffix: 
   1. For list view - `_list`
   2. For detail view - `_detail`
   - Create templates for manufacturer list, car list, driver list. In these
templates:
       - Table with the information of each instance.
         1. In the car list set a link on the id field that leads to the car 
       detail page.
         2. In the driver list set a link on the username field that leads to the  
       driver detail page 
   - Create driver detail template:
       - Place information about all cars of the driver
   - Create car detail template:
       - Place information about the manufacturer of the car (name, country)
       - Place information about all drivers of that car.
   - Inside `templates` create directory `includes`, create `sidebar.html` 
   there. In this file place links to the home page, manufacturer list page,
   car list page, drivers list page. Also, create `pagination.html` for the 
   pagination purpose and include this template in block `pagination` inside
   `base.html`.
   - In `base.html` include `sidebar.html` in block `sidebar`, so all these
   links will be accessible on all pages.
    
