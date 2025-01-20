"""
test checking notebook_vars function
"""

from pathlib import Path
import pytest

from open_atmos_jupyter_utils import notebook_vars
import examples

@pytest.fixture(scope="session", name="notebook_variables")
def notebook_variables_fixture():
    """returns variables from the notebook """
    print(examples.__file__)
    return notebook_vars(
        file=Path(examples.__file__).parent / "notebook_vars_example.ipynb",
        plot=False,
    )

def test_notebook_vars(notebook_variables):
    """ checks for a value known only after notebook execution"""
    assert notebook_variables["c"] == notebook_variables["a"] + notebook_variables["b"]
