# tRNAnalysis

<p align="left">
	<a href="https://readthedocs.org/projects/trnanalysis/badge/?version=latest", alt="Documentation">
		<img src="https://readthedocs.org/projects/trnanalysis/badge/?version=latest" /></a>
	<a href="https://travis-ci.com/Acribbs/tRNAnalysis.svg?branch=master", alt="Travis">
		<img src="https://api.travis-ci.com/Acribbs/tRNAnalysis.svg?branch=master" /></a>
	<a href="https://twitter.com/CribbsP?lang=en", alt="Twitter followers">
		<img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter" /></a>
	<a href="https://twitter.com/CribbsP?lang=en", alt="Twitter followers">
		<img src="https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter" /></a>
</p>

This workflow was generated as a response to not being able to effectively analyse tRNA data from next generation sequencing experiments rapidly and robustly. Typical workflows are not very flexible and do not scale well for multiple samples. Moreover, most do not impliment best-practice mapping strategies or generate detailed analysis reports to aid biological interpretation.

Our pipeline can be used for evaluating the levels of small RNAs in a sample, but provides detailed analysis of tRNAs, with particular emphasis on tRNA fragment analysis.The pipeline is in constant development and further features will be added in the future. For example, we will extend our pipeline to perform detailed anaysis of miRNAs and plan to write an R shiny framework for interactive report features.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed the latest version of conda ([Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anadonda](https://anaconda.org))
* You have a Linux or Mac machine. tRNAnalysis has been tested on Redhat linux and OSX Mojave.
* You have read the [documentation](https://trnanalysis.readthedocs.io/en/latest/)
* You have read the [preprint](https://www.biorxiv.org/content/10.1101/655829v1?rss=1)

## Documentation

Further help that introduces tRNAnalysis and provides a tutorial of how to run example
code can be found at [read the docs](https://trnanalysis.readthedocs.io/en/latest/)

## Installation of tRNAnalysis


### Conda installation

The preferred method for installing tRNAnalysis using [Conda](https://conda.io), through the [bioconda](https://bioconda.github.io) channel.

We have been experiencing issues with installation because of channel prioirities. Bioconda recommend that the channel priority for conda be set by runnig the following in the terminal::


	conda config --add channels defaults
	conda config --add channels bioconda
	conda config --add channels conda-forge

Then tRNAnalysis can be installed as follows::
    
    conda create -n trnanalysis
    conda activate trnanalysis
    conda install -c bioconda trnanalysis
    
Please look at 'previous installation issues' of the documentation for common installation issues, if you come acorss your own then please fell free to raise an [issue](https://github.com/Acribbs/tRNAnalysis/issues). 

### Conda solving issues 

Conda is an awesome project, however it can suffer from significant issues relating to how long it takes the solver to
fix installation issues. For more information regarding these conda issues please see [bioconda issues](https://github.com/conda/conda/issues/7239).

Solving issues are unfortiunately out of our hands and you shouyld follow recomendations from bioconda. It may be that you will need to install through pip or manually install the package following the instructions below. 

### Pip installation

trnanalysis can also be installed using pip::

    pip install trnanalysis


### Manual installation

Alternatively, you can manusally install tRNAnalysis by::

    git clone https://github.com/Acribbs/tRNAnalysis.git
    cd tRNAnalysis
    python setup.py install
    trnanalysis --help
    
## Usage

Further usage instructions can be accessed in the [documentation](https://trnanalysis.readthedocs.io/en/latest/).

Run the ``trnanalysis --help`` command view the help documentation for how to run tRNAnalysis.

To run the main trnanalysis pipeline run::

    trnanalysis make full -v5

In order to run and generate the multiQC report to identify read quality and Rmarkdown html report
for the tRNA analysis run::

    trnanalysis make build_report -v5
    
Running locally or on a cluster - the default setting to run trnanalysis is on a cluster, with SLURM, SGC, Torque and PBS/pro
currently supported. However, if you dont have access to a cluster then tRNAnalsysis can be executed locally by adding `--no-cluster` as a commandline argument::

	trnanalysis make full -v5 --no-cluster
