# open-atmos-jupyter-utils

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Github Actions Status](https://github.com/open-atmos/jupyter-utils/workflows/Pylint/badge.svg?branch=main)](https://github.com/open-atmos/jupyter-utils/actions)
[![PyPI version](https://badge.fury.io/py/open-atmos-jupyter-utils.svg)](https://pypi.org/project/open-atmos-jupyter-utils)
[![Github repo](https://img.shields.io/badge/jupyter--utils-code_repository-gold?logo=github)](https://github.com/open-atmos/jupyter-utils)

`open-atmos-jupyter-utils` is a Python package designed to provide utility routines that enhance the use of Jupyter notebooks in research and development workflows. 

## Features
- Improved Visualization Handling: Display inline vector graphics and animations and embed them in Jupyter notebooks which is compatible with GitHub, Jupyter Book and Colab.
- Integration with Automated Testing: The package enables the execution of notebook code as part of automated test suites (pytest framework). This helps maintain robust regression tests while keeping the notebooks intact.
- Pytest Integration: The notebook_vars() function allows for the execution of notebook code once during test sessions, enabling the reuse of final notebook states across multiple automated tests.

## Functions
- [``show_plot()``](https://open-atmos.github.io/jupyter-utils/open_atmos_jupyter_utils/show_plot.html) - a drop-in replacement for matplotlib.pyplot.show() that displays figures inline as SVG vector graphics. The function also provides a download widget that allows users to download the figure as PDF or SVG. On Google Colab, the widget triggers a Google Drive download.
- [``show_anim()``](https://open-atmos.github.io/jupyter-utils/open_atmos_jupyter_utils/show_anim.html) - a replacement for matplotlib.animation.FuncAnimation that displays inline animations in GIF format (which is compatible with GitHub rendering). It also provides a download widget to save the animation as a .gif file, with Colab support for Google Drive download.
- [``TemporaryFile``](https://open-atmos.github.io/jupyter-utils/open_atmos_jupyter_utils/temporary_file.html) - a class equipped with ``make_link_widget()`` method returning a click-to-download Colab-compatible widget to be display()-ed in a Jupyter notebook
- [``pip_install_on_colab('package_a', 'package_b', ...)``](https://open-atmos.github.io/jupyter-utils/open_atmos_jupyter_utils/pip_install_on_colab.html) - a function that automates the installation of Python packages in Colab environments via pip (and ldconfig for system libraries). This ensures smooth setup for notebooks running on Colab.
- [``notebook_vars``](https://open-atmos.github.io/jupyter-utils/open_atmos_jupyter_utils/notebook_vars) - a function that executes notebook code and returns a dictionary of variables present in the notebook. This is particularly useful for setting up automated tests using pytest fixtures without any modification to the original notebooks.

## Instalation
For instalation use:
```angular2html
pip install open-atmos-jupyter-utils
```
Then import inside Python project
```angular2html
import open_atmos_jupyter_utils as oaju
```
## Documentation
Public API docs are maintained at: https://open-atmos.github.io/jupyter-utils/


## Use Cases

open-atmos-jupyter-utils was developed and refined through the maintenance and enhancement of [PySDM](https://github.com/open-atmos/PySDM), [PyMPDATA](https://github.com/open-atmos/PyMPDATA) and [PyPartMC](https://github.com/open-atmos/PyPartMC) projects.
