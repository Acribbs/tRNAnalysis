.. _getting_started-Installation:


============
Installation
============

The following sections describe how to install tRNAnalysis. 

.. _getting_started-Conda:

Conda Installation
------------------

The our preffered method of installation is using conda. If you dont have conda installed then
please install conda using `miniconda <https://conda.io/miniconda.html>`_ or `anaconda <https://www.anaconda.com/download/#macos>`_.

tRNAnalysis is currently installed using the bioconda channel and the recipe can be found on `github `_. To install tRNAnalysis::

    conda install cgatcore

.. _getting_started-Automated:


Pip installation
----------------
We recommend installation through conda because it manages the dependancies. However, tRNAnalysis is 
generally lightweight and can be installed easily using pip package manager. However, you will also have to
install other dependancies manually::

	pip install trnanalysis

.. _getting_started-pip:

.. _getting_started-Manual:

Manual installation
-------------------

To obtain the latest code, check it out from the public git_ repository and activate it::

   git clone 
   cd 
   python setup.py develop

Once checked-out, you can get the latest changes via pulling::

   git pull 


.. _getting_started-Additional:

Installing additonal software
-----------------------------

When building your own workflows we recomend using conda to install software into your environment where possible.

This can easily be performed by::

   conda search <package>
   conda install <package>



.. _conda: https://conda.io
