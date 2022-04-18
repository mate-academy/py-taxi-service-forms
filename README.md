# Taxi service authentication 

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In this task, you will implement a custom form and django built-in forms for create,
update or delete content from the site.

1. Implement `Create`, `Update`, `Delete` views for `Driver`, `Car`, 
`Manufacturer`.
2. On driver list page create button that leads to the driver creation page.
3. Create a driver licence update page. The form on this page must check that 
licence:
    - Consist only of 8 characters
    - First 3 characters are uppercase letters
    - Last 5 characters are digits
4. On driver detail page add buttons that lead to update driver's licence page and
driver deletion page.
5. On car list page add button that leads to the car creation page. On car 
detail page add buttons that lead to car update page and car deletion page.
6. On manufacturer list page add button that leads to the manufacturer creation
page. Also, add columns `Update`, `Delete`, and add links for update page and 
deletion page for each manufacturer.
