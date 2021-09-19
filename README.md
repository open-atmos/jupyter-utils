# utils

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Github Actions Status](https://github.com/atmos-cloud-sim-uj/utils/workflows/Pylint/badge.svg?branch=main)](https://github.com/atmos-cloud-sim-uj/utils/actions)
[![PyPI version](https://badge.fury.io/py/atmos-cloud-sim-uj-utils.svg)](https://pypi.org/project/atmos-cloud-sim-uj-utils)

utility routines used in [PySDM](https://github.com/atmos-cloud-sim-uj/PySDM) and [PyMPDATA](https://github.com/atmos-cloud-sim-uj/PyMPDATA) example Jupyter notebooks:
- [``pip_install_on_colab('package_a', 'package_b', ...)``](https://atmos-cloud-sim-uj.github.io/utils/pip_install_on_colab.html) function handling execution of ``pip`` (and ``ldconfig``) on Colab 
- [``TemporaryFile``](https://atmos-cloud-sim-uj.github.io/utils/temporary_file.html) class equipped with ``make_link_widget()`` method returning a click-to-download Colab-compatible widget to be display()-ed in a Jupyter notebook
- [``show_plot()``](https://atmos-cloud-sim-uj.github.io/utils/show_plot.html) drop-in replacement for matplotlib's show() displaying the figure and a download-as-pdf widget just below

public API docs are maintained at: https://atmos-cloud-sim-uj.github.io/utils/
