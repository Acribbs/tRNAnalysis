.. _getting_started-Examples:


==================
Running a pipeline
==================


This section provides a tutorial-like introduction of how to run tRNAnalysis. It provides a toy example of
how the pipeline can be ran using test data. This can act as a showcase example of how you can modify the
configuration parameters so you are able to run your own pipeline.

.. _getting_started-Intro:

Introduction
=============

This pipeline requires the following input:

 * a single end fastq file - if you have paired end data we recoment flashing the reads together to make a single file or only using the first read of your paired end data.
 * a bowtie indexed genome
 * ensembl gtf: we recomend that you download out gtf files that have been sanitised for out pipeline `here <https://www.cgat.org/downloads/public/adam/data_trnanalysis/>`_.


**Optionally** to make the pipeline run faster you can also use a downloaded tRNAscan-SE output. The most time consuming part of the pipeline is running tScan-SE to identify tRNAs acorss the genome.
In order to speed the pipeline execution we have pre-ran tScan-SE and generated the outputs that can be
found in the following `directory <https://www.cgat.org/downloads/public/adam/data_trnanalysis/>`_ . You can then tell the pipeline the location of the file
using the yml configuration file.


.. _getting_started-setting-up-pipeline:

Setting up the pipeline
=======================

**Step 1**: Install tRNAnalysis:

Check that your computing environment is appropriate and follow tRNAnalysis installation instructions (see `Installation instructions <https://trnanalysis.readthedocs.io/en/latest/getting_started/Installation.html>`_).

**Step2**: To run a pipeline you will need to create a working directory
and enter it. For example::

   mkdir version1
   cd version1/

This is where the toy example pipeline will be executed and files will be generated in this
directory.

However, the tRNAnalysis example comes with test data and this can be downloaded by running::

	wget https://www.cgat.org/downloads/public/adam/trnanalysis/test_trna.tar.gz
	tar -zxvf test_trna.tar.gz
	cd test_trna

**Step 3**: Configure the cluster

Running pipelines on a cluster required the drmaa API settings to be configures and passed
to cgatcore. The default cluster engine is SGE, however we also support SLURM and Torque/PBSpro.
In order to execute using a non SGE cluster you will need to setup a `.cgat.yml` file in your
home directory and specify parameters according to the `cluster configuration documentation <https://cgat-core.readthedocs.io/en/latest/getting_started/Cluster_config.html>`_.

**Step 4**: Set up the configuration infomation

tRNAnalysis is written with minimal hard coded options. Therefore,
to run tRNAnalysis an initial configuration file needs to be
generated. A configuration file with all the default values can be obtained by
running::

      trnanalysis trna config


This will create a new :file:`pipeline.yml` file. **YOU MUST EDIT THIS
FILE**. The default values are unlikely to be configured correctly for your data. The
configuration file should be well documented in CGAT-core and the format is
a simple yaml file. 

In addition, to run differential expression analysis you will need to
generate a file called `meta_data.csv`, and this file should be placed in 
the directory where the pipeline will be executed. The tutorial provides an example
of how this can be formatted. The convention is as follows:

Sample, Condition, sample_type
CELL_NAME1, treatment1, cell1
CELL_NAME2, treatemnt2, cell1

**Step 5**: Add the input files (fastqs, tScan-SE file (can be downloaded from our `ftp server <https://www.cgat.org/downloads/public/adam/data_trnanalysis/>`_)). The input files are required to be in the directory that tRNAnalysis will be ran in. In the tutorial this is already done for you.

**Step 6**: You can check if all the external dependencies to tools and
R packages are satisfied by running::

      trnanalysis trna check

.. _getting_started-pipelineRunning:

Running tRNAnalysis
===================

Command line usage information is available by running::

   trnanalysis trna --help
   

The basic syntax for running tRNAnalysis is::

   trnanalysis trna [workflow options] [workflow arguments]


``workflow options`` can be one of the following:

make <task>

   run all tasks required to build task

show <task>

   show tasks required to build task without executing them

plot <task>

   plot image of workflow (requires `inkscape <http://inkscape.org/>`_) of
   pipeline state for task

touch <task>

   touch files without running task or its pre-requisites. This sets the 
   timestamps for files in task and its pre-requisites such that they will 
   seem up-to-date to the pipeline.

config

   write a new configuration file :file:`pipeline.ini` with
   default values. An existing configuration file will not be
   overwritten.

clone <srcdir>

   clone a pipeline from :file:`srcdir` into the current
   directory. Cloning attempts to conserve disk space by linking.


Fastq naming convention
-----------------------

tRNAanalysis assume that input fastq files follows the following
naming convention(with the read inserted between the fastq and the gz). The reason
for this is so that regular expressions do not have to acount for the read within the name.
It is also more explicit::

   sample1-condition-R1.fastq.1.gz
   sample1-condition-R2.fastq.2.gz


Additional options
------------------

In addition to running tRNAanalysis with default command line options, running trnaanalysis 
with --help will allow you to see additional options for ``workflow arguments``
when running the pipelines. These will modify the way the pipeline in ran.

`- -no-cluster`

    This option allows the pipeline to run locally.

`- -input-validation`

    This option will check the pipeline.ini file for missing values before the
    pipeline starts.

`- -debug`

    Add debugging information to the console and not the logfile

`- -dry-run`

    Perform a dry run of the pipeline (do not execute shell commands)

`- -exceptions`

    Echo exceptions immidietly as they occur.

`-c - -checksums`

    Set the level of ruffus checksums.

.. _getting_started-Building-reports:


Building tRNAnalysis reports
============================

Reports are generated using the following command once a the `full` command has completed::

    tranalysis trna make build_report


.. _getting_started-Troubleshooting:

Troubleshooting
===============

Many things can go wrong while running the pipeline. Look out for

   * bad input format. The pipeline does not perform sanity checks on the input format.  If the input is bad, you might see wrong or missing results or an error message.
   * pipeline disruptions. Problems with the cluster, the file system or the controlling terminal might all cause the pipeline to abort.
   * bugs. The pipeline makes many implicit assumptions about the input files and the programs it runs. If program versions change or inputs change, the pipeline might not be able to deal with it.  The result will be wrong or missing results or an error message.

If tRNAnalysis aborts, locate the step that caused the error by
reading the logfiles and the error messages on stderr
(:file:`nohup.out`). See if you can understand the error and guess the
likely problem (new program versions, badly formatted input, ...). If
you are able to fix the error, remove the output files of the step in
which the error occured and restart the pipeline. Processing should
resume at the appropriate point.

.. note:: 

   Look out for upstream errors. For example, the pipeline might build
   a geneset filtering by a certain set of contigs. If the contig
   names do not match, the geneset will be empty, but the geneset
   building step might conclude successfully. However, you might get
   an error in any of the downstream steps complaining that the gene
   set is empty. To fix this, fix the error and delete the files
   created by the geneset building step and not just the step that
   threw the error.

Common errors
-------------

One of the most common errors when runnig the tRNAnalysis is::

    GLOBAL_SESSION = drmaa.Session()
    NameError: name 'drmaa' is not defined

This error occurrs because you are not connected to the cluster. Alternatively
you can run the pipleine in local mode by adding `- -no-cluster` as a command line option.



.. _pipelineReporting:
