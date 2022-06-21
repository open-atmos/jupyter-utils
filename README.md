# utils

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Github Actions Status](https://github.com/atmos-cloud-sim-uj/utils/workflows/Pylint/badge.svg?branch=main)](https://github.com/atmos-cloud-sim-uj/utils/actions)
[![PyPI version](https://badge.fury.io/py/atmos-cloud-sim-uj-utils.svg)](https://pypi.org/project/atmos-cloud-sim-uj-utils)

Utility routines used in Jupyter notebooks in [PySDM-examples](https://github.com/atmos-cloud-sim-uj/PySDM-examples), [PyMPDATA-examples](https://github.com/atmos-cloud-sim-uj/PyMPDATA-examples) and [PyPartMC-examples](https://github.com/open-atmos/PyPartMC-examples) projects:
- [``show_plot()``](https://atmos-cloud-sim-uj.github.io/utils/show_plot.html) - a drop-in replacement for matplotlib's show() displaying the figure using vector graphics (svg) by default and offering a download-as-pdf widget just below (on Colab the widget triggers Google Drive download)
- [``TemporaryFile``](https://atmos-cloud-sim-uj.github.io/utils/temporary_file.html) - a class equipped with ``make_link_widget()`` method returning a click-to-download Colab-compatible widget to be display()-ed in a Jupyter notebook
- [``pip_install_on_colab('package_a', 'package_b', ...)``](https://atmos-cloud-sim-uj.github.io/utils/pip_install_on_colab.html) - a function handling execution of ``pip`` (and ``ldconfig``) on Colab 

public API docs are maintained at: https://atmos-cloud-sim-uj.github.io/utils/
