# Check Your Code Against the Following Points

## Code Style

1. Ensure each file ends with a single blank line.

2. Add a blank line between different groups of imports and ensure appropriate ordering of imports.
    
 Imports should be grouped in the following order:

    1.Standard library imports.
    2.Related third party imports.
    3.Local application/library specific imports.

Good example

```python
from django.urls import path

from taxi.views import index
```

Bad example:

```python
from django.urls import path
from taxi.views import index
```

3. Use absolute imports instead of relative imports 
  
Good example:


```python
from taxi.views import index
```

Bad example:

```python
from .views import index
```
## Clean Code

1. Don't forget to delete comments when you are ready to commit and push your code.