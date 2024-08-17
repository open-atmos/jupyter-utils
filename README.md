# open-atmos-jupyter-utils

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Github Actions Status](https://github.com/open-atmos/jupyter-utils/workflows/Pylint/badge.svg?branch=main)](https://github.com/open-atmos/jupyter-utils/actions)
[![PyPI version](https://badge.fury.io/py/open-atmos-jupyter-utils.svg)](https://pypi.org/project/open-atmos-jupyter-utils)

Utility routines used in Jupyter notebooks in [PySDM](https://github.com/open-atmos/PySDM), [PyMPDATA](https://github.com/open-atmos/PyMPDATA) and [PyPartMC](https://github.com/open-atmos/PyPartMC) projects:
- [``show_plot()``](https://open-atmos.github.io/jupyter-utils/show_plot.html) - a drop-in replacement for matplotlib's show() displaying the figure inline using vector graphics (svg) by default and offering a download-as-pdf-or-svg widget just below (on Colab the widget triggers Google Drive download)
- [``TemporaryFile``](https://open-atmos.github.io/jupyter-utils/temporary_file.html) - a class equipped with ``make_link_widget()`` method returning a click-to-download Colab-compatible widget to be display()-ed in a Jupyter notebook
- [``pip_install_on_colab('package_a', 'package_b', ...)``](https://open-atmos.github.io/jupyter-utils/pip_install_on_colab.html) - a function handling execution of ``pip`` (and ``ldconfig``) on Colab 

public API docs are maintained at: https://open-atmos.github.io/jupyter-utils/
