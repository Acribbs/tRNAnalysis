import setuptools
import sys
import os
from setuptools import setup, find_packages, Extension


from distutils.version import LooseVersion
if LooseVersion(setuptools.__version__) < LooseVersion('1.1'):
    print("Version detected:", LooseVersion(setuptools.__version__))
    raise ImportError(
        "the CGAT code collection requires setuptools 1.1 higher")


with open("README.md", "r") as fh:
    long_description = fh.read()

########################################################################
########################################################################
# Import setuptools
# Use existing setuptools, otherwise try ez_setup.
try:
    import setuptools
except ImportError:
    # try to get via ez_setup
    # ez_setup did not work on all machines tested as
    # it uses curl with https protocol, which is not
    # enabled in ScientificLinux
    import ez_setup
    ez_setup.use_setuptools()

########################################################################
########################################################################
IS_OSX = sys.platform == 'darwin'

########################################################################
########################################################################
# collect CGAT version
sys.path.insert(0, "cgatshowcase")
import version

version = version.__version__

###############################################################
###############################################################
# Define dependencies
#
major, minor1, minor2, s, tmp = sys.version_info

if major < 3:
    raise SystemExit("""cgat-showcase requires Python 3 or later.""")


cgat_package_dirs = {'cgatshowcase': 'cgatshowcase'}

##########################################################
##########################################################
# Classifiers
classifiers = """
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved
Programming Language :: Python
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

setup(
    # package information
    name='cgatshowcase',
    version=version,
    description='cgatshowcase : the Computational Genomics Analysis Toolkit example pipeline/workflow',
    author='Adam Cribbs',
    author_email='adam.cribbs@imm.ox.ac.uk',
    license="MIT",
    platforms=["any"],
    keywords="computational genomics",
    long_description=long_description,
    classifiers=[_f for _f in classifiers.split("\n") if _f],
    url="https://github.com/cgat-developers/cgat-showcase",
    # package contents
    packages=find_packages(),
    package_data={'cgatshowcase':['cgatshowcase/R/*.R', 'cgatshowcase/pipeline_docs/pipeline_transdiffexprs/R_report.dir/*', '/cgatshowcase/pipeline_transdiffexprs/*']},
    package_dir=cgat_package_dirs,
    include_package_data=True,
    entry_points={
        'console_scripts': ['cgatshowcase = cgatshowcase.entry:main']
    },
    # other options
    zip_safe=False,
    test_suite="tests",
    
)
