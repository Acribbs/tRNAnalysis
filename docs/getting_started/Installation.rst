.. _getting_started-Installation:


============
Installation
============

The following sections describe how to install tRNAnalysis. 

.. _getting_started-Conda:

Conda Installation
------------------

The our preffered method of installation is using conda. However, at the moment we have had to pin one of the projects and
it takes a while for the solver to install the project. Threfore, if the installation does take a long time it
may be better to follow the **Conda environment** installation instructions. If you dont have conda installed then
please install conda using `miniconda <https://conda.io/miniconda.html>`_ or `anaconda <https://www.anaconda.com/download/#macos>`_.

tRNAnalysis is currently installed using the bioconda channel and the recipe can be found on `github `_. To install tRNAnalysis::

    conda install - bioconda trnanalysis

Please check that cgat-apps is version 0.5.3 and not 0.5.4. If you have this installed then please run::

    conda install cgat-apps=0.5.3

Temporarily, we have also hosted a linux version only on anaconda which can downloaded as follows::

    conda install -c cgat trnanalysis

Conda environment
-----------------

Conda is an awesome project, however it can suffer from significant issues relating to how long it takes the solver to
fix installation issues. For more information regarding these conda issues please see `bioconda issues <https://github.com/conda/conda/issues/7239>`_.

In order to try and speed things up we have provided a conda environment for installation. Currently only linux is supported and it can
be installed by doing the following::

    wget https://raw.githubusercontent.com/Acribbs/tRNAnalysis/master/conda/environments/trnanalysis-linux.yml
    conda env create -f trnanalysis-linux.yml 
    conda activate trnanalysis-env

.. _getting_started-Automated:


Pip installation
----------------
We recommend installation through conda because it manages the dependencies. Despite this, tRNAnalysis
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
