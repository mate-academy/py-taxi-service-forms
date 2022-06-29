# Taxi service home page

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

In this task, you should implement the home page of the site.

1. Inside `taxi_service.urls` add path to the `taxi.urls`. Don't forget to specify `namespace`.
2. Inside `taxi.urls` create a path for the home page. This
page should open when you are accessing `http://127.0.0.1:8000/`. Give this
path the name `index`.
3. Inside `taxi.views` create function `index`. In this function:
    - count the number of all drivers
    - count the number of all manufacturers
    - count the number of all cars
    - return `HttpResponse` with rendered template. Pass received data to this template.
4. Before you create a template you have to create styles for the 
template. Create directory `static` next to directory `taxi`. Inside this 
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
      - Create block `pagination`
7. Inside `templates` create a directory `taxi`. There you will store templates
for the app `taxi`. Create `index.html` there. Inside `index.html`:
    - Override block `content` and place (as a list) information about:
        - Number of cars
        - Number of drivers
        - Number of manufacturers
8. Create some drivers, manufacturers, and cars. Run server, open 
`http://127.0.0.1:8000/`, check if the information is there and if it is 
correct.

NOTE: Attach screenshots of all created or modified pages to pull request. It's important to attach images not links to them. See example:

![image](https://mate-academy-images.s3.eu-central-1.amazonaws.com/python_pr_with_images.png)
