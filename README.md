# open-atmos-jupyter-utils

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Github Actions Status](https://github.com/open-atmos/jupyter-utils/workflows/Pylint/badge.svg?branch=main)](https://github.com/open-atmos/jupyter-utils/actions)
[![PyPI version](https://badge.fury.io/py/open-atmos-jupyter-utils.svg)](https://pypi.org/project/open-atmos-jupyter-utils)
[![Github repo](https://img.shields.io/badge/jupyter--utils-code_repository-gold?logo=github)](https://github.com/open-atmos/jupyter-utils)

## Features

`open-atmos-jupyter-utils` is a Python package providing Jupyter notebook utility routines 
for:
- presenting [matplotlib](https://matplotlib.org) plots as either SVG vector graphics or animated GIFs, embedding them within the notebooks, and rendering correctly in [GitHub's Rich Jupyter Notebook diffs](https://github.blog/changelog/2023-03-01-feature-preview-rich-jupyter-notebook-diffs/)
- save-as buttons below each figure (triggering [Google-Drive downloads](https://colab.research.google.com/notebooks/io.ipynb#scrollTo=hauvGV4hV-Mh) on [Colab](https://colab.google/))
- execution of unmodified notebook code for automated testing (e.g., within [pytest fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html))
- pip-installation of external packages on Colab safeguarded against [alterations of Google-shipped packages](https://github.com/googlecolab/colabtools/issues/2837)

## Functions and Examples
- [``show_plot()``](https://open-atmos.github.io/jupyter-utils/open_atmos_jupyter_utils/show_plot.html) - a drop-in replacement for matplotlib.pyplot.show() that displays figures inline as SVG vector graphics. The function also provides a download widget that allows users to download the figure as PDF or SVG. On Google Colab, the widget triggers a Google Drive download. Example:   
  [![preview notebook](https://img.shields.io/static/v1?label=render%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/jupyter-utils/blob/main/examples/show_plot.ipynb)
  [![launch on mybinder.org](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/open-atmos/jupyter-utils.git/main?urlpath=lab/tree/examples/show_plot.ipynb)
  [![launch on Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-atmos/jupyter-utils/blob/main/examples/show_plot.ipynb)
- [``show_anim(plot_func: typing.Callable, frame_range: typing.Iterable)``](https://open-atmos.github.io/jupyter-utils/open_atmos_jupyter_utils/show_anim.html) - a replacement for matplotlib.animation.FuncAnimation that displays inline animations in GIF format (which is compatible with GitHub rendering). It also provides a download widget to save the animation as a GIF file, with Colab support for Google Drive download. Example:  
  [![preview notebook](https://img.shields.io/static/v1?label=render%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/jupyter-utils/blob/main/examples/show_anim.ipynb)
  [![launch on mybinder.org](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/open-atmos/jupyter-utils.git/main?urlpath=lab/tree/examples/show_anim.ipynb)
  [![launch on Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/open-atmos/jupyter-utils/blob/main/examples/show_anim.ipynb)
- [``notebook_vars(notebook: pathlib.Path, plot: bool)``](https://open-atmos.github.io/jupyter-utils/open_atmos_jupyter_utils/notebook_vars) - a function that executes notebook code and returns a dictionary of variables present in the notebook. This is particularly useful for setting up automated tests using pytest fixtures without any modification to the original notebooks. The `plot` flag controls if `show_plot()` calls within the notebook should be run or not. Example:   
    [![view test](https://img.shields.io/static/v1?label=view%20on&logo=github&color=87ce3e&message=GitHub)](https://github.com/open-atmos/jupyter-utils/blob/main/tests/test_notebook_vars.py)
- [``pip_install_on_colab('package_a', 'package_b', ...)``](https://open-atmos.github.io/jupyter-utils/open_atmos_jupyter_utils/pip_install_on_colab.html) - a function that automates the installation of Python packages in Colab environments via pip (and ldconfig for system libraries). This ensures smooth setup for notebooks running on Colab.

## Usage
For installation use:
```bash
pip install open-atmos-jupyter-utils
```
Then import inside Python project
```Python
import open_atmos_jupyter_utils as oaju
```

## Documentation
Public API docs are maintained at: https://open-atmos.github.io/jupyter-utils/


## Use Cases
open-atmos-jupyter-utils has been developed for and used in numerous Jupyter
notebooks in [PySDM](https://github.com/open-atmos/PySDM), [PyMPDATA](https://github.com/open-atmos/PyMPDATA) and [PyPartMC](https://github.com/open-atmos/PyPartMC) projects.
