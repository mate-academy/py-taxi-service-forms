# Taxi service forms

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In this task, you will implement a custom form and django built-in forms to create,
update or delete content from the site.

1. Implement:
    - `Create`, `Update`, `Delete` views for `Car`, 
    - `Create`, `Update`, `Delete` views for `Manufacturer`, 
    - `Create`, `Delete` views for `Driver`, 
2. On the driver list page create a button that leads to the driver creation page.
3. Create a driver's license update page. The form on this page must check that 
license:
    - Consist only of 8 characters
    - First 3 characters are uppercase letters
    - Last 5 characters are digits
4. On the driver detail page add buttons that lead to the driver's license updating page and
driver deletion page.
5. On the car list page add button that leads to the car creation page. On the car 
detail page, add buttons that lead to the car update page and car deletion page.
6. On the manufacturer list page, add the button that leads to the manufacturer creation
page. Also, add columns `Update`, `Delete`, and add links for the updating page and 
deletion page for each manufacturer.
