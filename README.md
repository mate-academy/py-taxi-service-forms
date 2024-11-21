# Taxi service home page

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start
- Use the following command to load prepared data from fixture to test and debug your code:

  ```python manage.py loaddata taxi_service_db_data.json```.

Feel free to add more data using admin panel, if needed.

In this task, you should implement the home page of the site.

1. Inside `taxi_service.urls` add path to the `taxi.urls`. Don't forget to specify `namespace`.
2. Inside `taxi.urls` create a path for the home page. This
page should open when you are accessing `http://127.0.0.1:8000/`. Give this
path the name `index`.
3. Inside `taxi.views` create function `index`. In this function:
    - count the number of all drivers with `num_drivers` variable
    - count the number of all manufacturers with `num_manufacturers` variable
    - count the number of all cars with `num_cars` variable 
    - return `HttpResponse` with rendered template. Pass received data to this template (don't import `HttpResponse` if you use `render`, this import is unnecessary).

4. Before you create a template you have to create styles for the 
template. Create directory `static` next to the directory `taxi`. Inside this 
directory create a file with the following path `css/styles.css`. Don't forget to do all necessary steps so that Django can serve these static files.
5. Create directory `templates` next to the directory `taxi`. There you will
store templates for pages. Edit settings so that engine knows where to look for template source files.
6. Inside directory `templates` create template `base.html`, it is a parent 
template, other templates will extend `base.html`. Inside `base.html`:
   - Inside `<head>`:
      - Create block `title` with `Taxi Service` title inside
      - Load static and import `styles.css`
   - Inside `<body>`:
      - Create block `sidebar`
      - Create block `content`
7. Inside `templates` create a directory `taxi`. There you will store templates
for the app `taxi`. Create `index.html` there. Inside `index.html`:
    - Override block `content` and place (as a list) information about:
        - Number of cars
        - Number of drivers
        - Number of manufacturers
8. Inside `templates` create a directory `includes`. There you will store includes. 
Create `sidebar.html` there. Inside `sidebar.html`:
    - Write realization of `sidebar` include that must have a list of empty links:
        - Home page
        - Manufacturers
        - Cars
        - Drivers
    - Anchor tags can serve as placeholder links for this task, meaning the actual destination of the link is not a concern.
      For example, you can use `href="#"` as the link destination.

    - In `base.html` include `sidebar.html`, so all these links will be accessible on all pages.
9. Check that you put empty lines at the end of each HTML file.
10. Run server, open `http://127.0.0.1:8000/`, check if the information is there and if it is correct.
11. Run `python manage.py test` to check your code results.
12. Avoid adding unnecessary files (like `venv`, `pycache`, `.idea`, `db.sqlite3`) and remember to include a `.gitignore` file in your PR.

### Note: Attach screenshots of all created or modified pages to pull request. 

1) Attach screenshots to the comment, NOT in commit. 
2) It's important to **attach images** not links to them. See example:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)
