.. _getting_started-Installation:


============
Installation
============

The following sections describe how to install tRNAnalysis.

.. _getting_started-Conda:

Conda Installation
------------------

The our preferred method of installation is using conda. If you dont have conda installed then
please install conda using `miniconda <https://conda.io/miniconda.html>`_ or `anaconda <https://www.anaconda.com/download/#macos>`_.

We have been experiencing issues with installation because of channel priorities.
Bioconda recommend that the channel priority for conda be set by running the following in the terminal::

  conda config --add channels defaults
  conda config --add channels bioconda
  conda config --add channels conda-forge

tRNAnalysis is currently installed using the bioconda channel and the recipe can be found on `github`_.

To install tRNAnalysis::

  conda create -n trnanalysis
  conda activate trnanalysis
  conda install -c bioconda trnanalysis


Pip installation
----------------
We recommend installation through conda because it manages the dependencies. However, tRNAnalysis
can also be installed easily using the pip package manager. However, you will also have to
install other dependencies manually::

	pip install trnanalysis

.. _getting_started-pip:

.. _getting_started-Manual:

Manual installation
-------------------

To obtain the latest code, check it out from the public git repository and activate it::

   git clone https://github.com/Acribbs/tRNAnalysis.git
   cd tRNAnalysis
   python setup.py install

Once checked-out, you can get the latest changes via pulling::

   git pull origin master


.. _getting_started-Additional:

Installing additonal software
-----------------------------

When building your own workflows we recomend using conda to install software into your environment where possible.

This can easily be performed by::

   conda search <package>
   conda install <package>



.. _conda: https://conda.io
