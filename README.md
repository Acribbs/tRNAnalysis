
![cgat-showcase](https://github.com/cgat-developers/cgat-showcase/blob/master/docs/img/CGAT_showcase.png)
=======


cgat-showcase is a repository containing an example pipeline constructed to demonstrate how the [cgat-core](https://github.com/cgat-developers/cgat-core) workflow management system can be used to create common workflows required in bioinformatics analysis.

Within this repository is an example [pipeline](https://github.com/cgat-developers/cgat-showcase/blob/master/cgatshowcase/pipeline_transdiffexprs.py) `pipeline_transdiffexprs.py` that performs pseudoalignment of fastq files
with [kallisto](https://pachterlab.github.io/kallisto/about.html) and differential expression using [DESeq2](https://www.bioconductor.org/packages/release/bioc/html/DESeq2.html). It can be run locally on your own machine or distributed across a cluster depending on your requirements.

Documentation on how to run this pipeline can be found [here](https://cgat-showcase.readthedocs.io/en/latest/) and documentation on how
to build your own custom workflow from scratch can be found [here](https://cgat-core.readthedocs.io/en/latest/defining_workflow/Tutorial.html).

Installation
------------

The following sections describe how to install the cgat-showcase pipeline.

We recommend installing using conda and the steps are described below::

   `conda install -c cgat cgatshowcase`

Alternatively, the pipeline can be installed using pip::

   `pip install cgatshowcase`

However, you will require certain software to run the pipeline. More detail on installation can be found on the [Installation](https://cgat-showcase.readthedocs.io/en/latest/getting_started/Installation.html) documentation.

Installation issues
-------------------

Conda installation can be quite slow (particularly for linux) and this is primarily an issue 
with the conda solver, which is known and conda developers are working on making it faster, so if installation
is taking a long time then try to install using one of our conda-envs 
(see conda-envs/environment-mac.yml or conda-envs/environment-linux.yml).

	`conda env create -f [environment-mac.yml/environment-linux.yml]`
