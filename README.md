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

## Installation


### Conda installation

The preferred method for installing tRNAnalysis is through [Conda](https://conda.io). 

To install trnanalysis using conda::
    
    conda install -c bioconda trnanalysis

### Manual installation

Alternatively, you can manusally install tRNAnalysis by::

    git clone https://github.com/Acribbs/tRNAnalysis.git
    cd tRNAnalysis
    python setup.py install
    trnanalysis --help
    
## Usage

Run the ``trnanalysis --help`` command view the help documentation for how to run tRNAnalysis.

To run the main trnanalysis pipeline run::

    trnanalysis trna make full -v5

In order to run and generate the multiQC report to identify read quality and Rmarkdown html report
for the tRNA analysis run::

    trnanalysis trna make build_report -v5
    
Running locally or on a cluster - the default setting to run trnanalysis is on a cluster, with SLURM, SGC, Torque and PBS/pro
currently supported. However, if you dont have access to a cluster then tRNAnalsysis can be executed locally by adding `--no-cluster` as a 
commandline argument. 

## Documentation

Further help that introduces tRNAnalysis and provides a tutorial of how to run example
code can be found at [read the docs](https://trnanalysis.readthedocs.io/en/latest/)
