
[![](https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }})

# {% if cookiecutter.logo_url %}<img src="{{ cookiecutter.logo_url }}" height="27px" align="left"></img>{% endif %} {{ cookiecutter.repo_name }}

## Overview

{{ cookiecutter.short_description }}

## Getting Started

Install `{{ cookiecutter.package_name }}`:

```
pip install {{ cookiecutter.package_name }}
```

A simple example:

```python
import {{ cookiecutter.package_directory }}

# Do something with {{ cookiecutter.package_directory }}
```

## Links

See the
[documentation here.](
https://{{ cookiecutter.repo_username }}.github.io/{{ cookiecutter.repo_name }}/
)

## Author

Created by {{ cookiecutter.package_author }}. MIT License.