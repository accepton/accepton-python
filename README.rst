AcceptOn
========

|circleci|

.. |circleci| image:: https://circleci.com/gh/accepton/accepton-python.svg?style=shield&circle-token=9a4878f9e5d7eb8ff1cbcfb863641772aa7e9005
   :target: https://circleci.com/gh/accepton/accepton-python
   :alt: Build Status

Documentation
-------------

Please see the `Python developer documentation`_ for more information.

.. _Python developer documentation: http://developers.accepton.com/?python

Installation
------------

Install from PyPI using `pip`_, a package manager for Python.

.. code-block:: bash

    $ pip install accepton

Don't have pip installed? Try installing it by running this from the
command line:

.. code-block:: bash

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

You may need to run the above commands with ``sudo``.

.. _pip: http://www.pip-installer.org/en/latest/

Contributing
------------

1. Fork it
2. Create your feature branch (``git checkout -b my-new-feature``)
3. Run the test suite on all supported Pythons (``tox``)
4. Run the code linter to find style violations (``tox -e pep8``)
5. Commit your changes (``git commit -am 'Add some feature'``)
6. Push the branch (``git push origin my-new-feature``)
7. Create a new Pull Request
