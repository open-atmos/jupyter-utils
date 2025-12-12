"""
test checking notebook_vars function
"""

from pathlib import Path
import pytest
import matplotlib


from open_atmos_jupyter_utils import notebook_vars

@pytest.fixture(scope="session", name="notebook_variables")
def notebook_variables_fixture():
    """returns variables from the notebook """
    return notebook_vars(
        file=str(Path(__file__).parent.parent / "examples" / "notebook_vars.ipynb"),
        plot=False,
    )
class TestNotebookVars:
    """test notebook_vars function"""
    @staticmethod
    def test_notebook_vars(notebook_variables):
        """ checks for a value known only after notebook execution"""
        assert notebook_variables["c"] == notebook_variables["a"] + notebook_variables["b"]

    @staticmethod
    def test_plots_closed(notebook_variables):
        """ checks all figures closed """
        assert isinstance(notebook_variables["fig"], matplotlib.figure.Figure) 
        assert 0 == len(matplotlib.pyplot.get_fignums())
