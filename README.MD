
### cleanipynb


[![](https://img.shields.io/pypi/v/clean_ipynb.svg)](https://pypi.python.org/pypi/cleanipynb)
[![](https://img.shields.io/travis/i008/clean_ipynb.svg)](https://travis-ci.org/i008/clean_ipynb)


This package will cleanup your jupyter notebook by:

- removing unused imports (globally)
- moving all imports to the first cell and reordering them
- reformatting your code with autopep8

All this with preserving the cell structure thanks to jupytext smart export to python features.




> **WARNING**: Cleaning happens in-place - Be careful


### Usage:

```bash
pip install cleanipynb
cleanipynb path_to_your_notebook.ipynb
```

### Demo:
![](beforeafter.gif)


### Credits:

- jupytext
- importanize
- autoflake
- autopep8
