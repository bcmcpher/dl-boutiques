"""DataLad Boutiques Extension"""

__docformat__ = 'restructuredtext'

import logging
lgr = logging.getLogger('datalad.boutiques')

# Defines a datalad command suite.
# This variable must be bound as a setuptools entrypoint
# to be found by datalad
command_suite = (
    # description of the command suite, displayed in cmdline help
    "DataLad Boutiques Command Suite",
    [
        # specification of a command, any number of commands can be defined
        (
            # importable module that contains the command implementation
            'datalad_boutiques.boutiques',
            # name of the command class implementation in above module
            'Boutiques',
            # optional name of the command in the cmdline API
            'boutiques',
            # optional name of the command in the Python API
            'boutiques'
        ),
    ]
)

from . import _version
__version__ = _version.get_versions()['version']
