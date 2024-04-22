"""
the magick behind ``pip install ...``
"""
from setuptools import setup, find_packages


def get_long_description():
    """returns contents of README.md file"""
    with open("README.md", "r", encoding="utf8") as file:
        long_description = file.read()
    return long_description


setup(
    name='open-atmos-jupyter-utils',
    description='utility routines used in PySDM, PyMPDATA and PyPartMC examples and tests',
    use_scm_version={
        "local_scheme": lambda _: "",
        "version_scheme": "post-release"
    },
    setup_requires=['setuptools_scm'],
    install_requires=['ipywidgets', 'IPython', 'matplotlib'],
    author='https://github.com/open-atmos/jupyter-utils/graphs/contributors',
    author_email='sylwester.arabas@agh.edu.pl',
    license="GPL-3.0",
    packages=find_packages(include=['open_atmos_jupyter_utils', 'open_atmos_jupyter_utils.*']),
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    project_urls={
        "Tracker": "https://github.com/open-atmos/jupyter-utils/issues",
        "Documentation": "https://open-atmos.github.io/jupyter-utils",
        "Source": "https://github.com/open-atmos/jupyter-utils"
    }
)
