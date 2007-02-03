"""pill (and zill) - twill extensions for use with zope & plone
"""

classifiers = """\
Development Status :: 3 - Alpha
Programming Language :: Python
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Libraries
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
"""

import sys
from distutils.core import setup

if sys.version_info < (2, 3):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

doclines = __doc__.split("\n")

setup(name="pill",
      version="0.1",
      maintainer="Petri Savolainen",
      maintainer_email="petri.savolainen@iki.fi",
      platforms = ["win32", "unix"],
      packages = ["pill"],
      package_dir = {"pill": "lib"},
      scripts=['scripts/demo.tw',],
      description = doclines[0],
      classifiers = filter(None, classifiers.split("\n")),
      long_description = "\n".join(doclines[2:]),
)
