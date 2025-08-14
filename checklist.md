# Сheck Your Code Against the Following Points

## Don't Push db files

Make sure you don't push db files (files with `.sqlite`, `.db3`, etc. extension).

## Don't forget to attach all screenshots of created/modified pages.

## Code Efficiency
Don't override `template_name`, `context_object_name` and so on if they are the same as default ones.

## Code Style
1. Make sure you've added a blank line at the end to all your files including `.css`, `.html` and `.gitignore`.
2. Use `()` instead of `backslash — \` in if-statements.

Good example:

```python
if (first_condition and second_condition 
        and third_condition):
    #  some actions
```

Also possible one:

```python
if (first_condition and
    second_condition):
    #  some actions
```

Bad example:

```python
if first_condition and second_condition \
    and third_condition:
    # some actions
```

3. Group imports using `()` if needed.

Good example:

```python
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin, 
    PermissionRequiredMixin,
)
```

Bad example:

```python
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin, PermissionRequiredMixin
```

4. Use correct path names.

Good example:

```python
path(
    "manufacurers/create/", 
    ManufacturerCreateView.as_view(), 
    name="manufacturer_form.html"
),
```

Bad example:

```python
path(
    "manufacturers/manufacturer_create/", 
    ManufacturerCreateView.as_view(), 
    name="manufacturer_form.html"
)
```

Another bad example:

```python
path("create/", ManufacturerCreateView.as_view(), name="manufacturer_form.html")
```

5. Add `Cancel` button apart from `Delete` one. The `Cancel` button will lead to the previous page the user was on.

6. Make sure you use 2 whitespaces indentations in your `.html` files.
7. Use `-` to split words in URL identification parameter `name`, not the `_`.

Good example:

```python
urlpatterns = [
    path("buses/", BusListView.as_view(), name="bus-list"),
]
 ```

Bad example:

```python
urlpatterns = [
    path("buses/", BusListView.as_view(), name="bus_list"),
]
 ```

## Clean Code
Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
