# pylint: disable=missing-module-docstring

from matplotlib import pyplot
from ipywidgets import HBox
from IPython.display import display
from IPython.core.interactiveshell import InteractiveShell
from IPython.core.pylabtools import select_figure_formats
from open_atmos_jupyter_utils.temporary_file import TemporaryFile


def show_plot(filename=None, fig=pyplot, inline_format='svg'):
    """ the missing click-to-save-as-pdf-or-svg button for matplotlib/Jupyter 
    (use instead of *.show()) """
    link = save_and_make_link(fig, filename)
    select_figure_formats(InteractiveShell.instance(), {inline_format})
    pyplot.show()
    display(link)


def save_and_make_link(fig, filename=None):
    """ saves a figure as pdf and returns a Jupyter display()-able click-to-download widget """
    temporary_files = [
        TemporaryFile(suffix=suffix, filename=(
            filename if filename is None or not filename.endswith('.pdf') else filename[:-4]
        ) + suffix)
        for suffix in ('.pdf', '.svg')
    ]
    for temporary_file in temporary_files:
        fig.savefig(temporary_file.absolute_path, bbox_inches='tight')
    return HBox([temporary_file.make_link_widget() for temporary_file in temporary_files])
