# pylint: disable-next=missing-module-docstring

from matplotlib import pyplot
from IPython.display import display
from atmos_cloud_sim_uj_utils.temporary_file import TemporaryFile


def show_plot(filename=None, fig=pyplot):
    """ the missing click-to-save-as-pdf button for matplotlib/Jupyter (use instead of *.show()) """
    link = save_and_make_link(fig, filename)
    pyplot.show()
    display(link)


def save_and_make_link(fig, filename=None):
    """ saves a figure as pdf and returns a Jupyter display()-able click-to-download widget """
    temporary_file = TemporaryFile(suffix='.pdf', filename=filename)
    fig.savefig(temporary_file.absolute_path, bbox_inches='tight')
    return temporary_file.make_link_widget()
