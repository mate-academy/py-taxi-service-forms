# Taxi service class-based views

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start
- Use the following command to load prepared data from fixture to test and debug your code:

  ```python manage.py loaddata taxi_service_db_data.json```

- After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.user`
  - Password: `1qazcde3`
- Make sure that you change the settings for [html-files](https://github.com/mate-academy/py-task-guideline/blob/main/html_settings/README.MD).
Use 2 indents in `.html` files.

Feel free to add more data using admin panel, if needed.

In this task, you should implement class-based list and detail views.

1. Create `ManufacturerListView` list view.
    - Set model on which the list view is built.
    - Set queryset, select all manufacturers, they should be ordered by name by default.
    - Set pagination equals to 5. It indicates how many instances should be displayed on a single page.

2. Create `CarListView` list view.
    - Set model, pagination equals to 5, queryset.
    - **Note**: Car model has foreign key `manufacturer`, so don't forget to improve query performance _(N+1 problem)_.

3. Create `CarDetailView` detail view.
    - Set only model.
    
4. Create `DriverListView` list view.
    - Set model and pagination equals to 5.

5. Create `DriverDetailView` detail view.
    - Set model and queryset.
    - In this view, you display information about cars of the driver. 
      **Optimize query**: don't make a query for a manufacturer for each car _(N+1 problem)_.

6. Inside `taxi/urls.py`:
   - Create such paths:
     - by `manufacturers/` you should get manufacturer list view;
     -  `cars/` - car list view;
     -  `cars/pk/` - car detail view;
     -  `drivers/` - driver list view;      
     -  `drivers/pk/` - driver detail view.

7. Create templates for the views. 
   - By default, class-based views try to find a template based on the model name and certain suffix: 
     1. For list view - `_list`
     2. For detail view - `_detail`
   - Create templates for manufacturer list, car list, driver list. In these templates:
       - Create table with the information of each instance.
         1. In the car list set a link on the id field that leads to the car detail page.
         2. In the driver list set a link on the username field that leads to the driver detail page.
   - Create driver detail template:
       - place information about all cars of the driver.
   - Create car detail template:
       - place information about the manufacturer of the car (name, country);
       - place information about all drivers of that car.
   - Inside `templates/includes`:
       - create `pagination.html` for the pagination purpose and include this template inside `base.html`;
       - in `sidebar.html` add links to the home page, manufacturer list page, car list page, drivers list page.
   - Check that you put empty lines at the end of each html-file.
    
8. Run server, open `http://127.0.0.1:8000/`, check if everything is displayed correctly.
9. Check that you put empty lines at the end of each HTML file.
10. Check your code style with `flake8`.
11. Run `python manage.py test` to check your code results.

### Note: Attach screenshots of all created or modified pages to pull request. 
it would be better to attach screenshots to the comment, NOT in commit. 
It's important to **attach images** not links to them. See example:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)
