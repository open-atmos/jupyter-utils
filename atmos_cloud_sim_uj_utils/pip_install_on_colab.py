# pylint: disable-next=missing-module-docstring

def pip_install_on_colab(*args):
    """executes pip (and ldconfig) ensuring Colab subtleties are handled as sane as it can get"""
    # pylint: disable-next=import-outside-toplevel
    # pylint: disable-next=multiple-imports
    import subprocess, notebook, tornado, sys
    subprocess.check_call([
      sys.executable, '-m', 'pip', '--quiet', '--use-deprecated=legacy-resolver', 'install',
      f'notebook=={notebook.__version__}',
      f'tornado=={tornado.version}',
      *args
    ])
    subprocess.check_call(['ldconfig'])
