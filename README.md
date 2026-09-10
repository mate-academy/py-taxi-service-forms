# Taxi service forms

Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.
- Make sure that you change the settings for [html-files](https://github.com/mate-academy/py-task-guideline/blob/main/html_settings/README.MD).
- Use the following command to load prepared data from fixture to test and debug your code:
  
`python manage.py loaddata taxi_service_db_data.json`

- After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.user`
  - Password: `1qazcde3`

Feel free to add more data using admin panel, if needed.

In this task, you will implement a custom form and django built-in forms to create,
update or delete content from the site.

1. Implement:
    - `Create`, `Update`, `Delete` views for `Car`, 
    - `Create`, `Update`, `Delete` views for `Manufacturer`.
2. On the car list page add button that leads to the car creation page. On the car 
detail page add buttons that lead to the car update page and car deletion page.
3. On the manufacturer list page, add the button that leads to the manufacturer creation
page. Also, add columns `Update`, `Delete`, and add links for the updating page and 
deletion page for each manufacturer.
4. Use crispy forms in your forms to make website more beautiful.

NOTE: Attach screenshots of all created or modified pages to pull request. It's important to attach images not links to them.

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.

# Note
Follow these steps if you need to use `crispy_forms` v2.0 with Python 3.11:

1. Add `CRISPY_TEMPLATE_PACK` to `settings.py`.

```python
CRISPY_TEMPLATE_PACK="bootstrap4"
```

2. Add these apps to `INSTALLED_APPS` and install them corresponding to the `CRISPY_TEMPLATE_PACK` bootstrap version.

```python
INSTALLED APPS = [
   ...,
   "crispy_bootstrap4",
   "crispy_forms",
]
```
