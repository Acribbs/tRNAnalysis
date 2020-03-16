.. _getting_started-Examples:


==================
Running a pipeline
==================


Running tRNAnalysis is easy using the commandline. If you have installed trnanalysis using conda then
all the software dependancies should have been installed and you are ready to go. A step by step tutorial
pipeline can be found `here: <https://trnanalysis.readthedocs.io/en/latest/getting_started/Tutorial.html>`_.

.. _getting_started-Intro:

Introduction
=============

This pipeline requires the following input:

 * a single end fastq file - if you have paired end data we recommend flashing the reads together to make a single file or only using the first read of your paired end data.
 * a bowtie indexed genome
 * ensembl gtf: we recommend that you download our gtf files that have been sanitised for this workflow `here <https://www.cgat.org/downloads/public/adam/data_trnanalysis/>`_. However,
 you can use your own, if you make sure that all of the chromosomes are listed according to the ensembl annotations (i.e. the chromosomes are named chr1, chr2.. e.c.t.)


**Optionally** to make the pipeline run faster you can also use a downloaded tRNAscan-SE output. The most time consuming part of the pipeline is running tScan-SE to identify tRNAs across the genome.
In order to speed the pipeline execution we have pre-ran tScan-SE and generated the outputs that can be
found in the following `directory <https://www.cgat.org/downloads/public/adam/data_trnanalysis/>`_ . You can then tell the pipeline the location of the file
using the yml configuration file.


.. _getting_started-setting-up-pipeline:

Running tRNAnalysis
===================

Command line usage information is available by running::

   trnanalysis --help


The basic syntax for running tRNAnalysis is::

   trnanalysis [workflow options] [workflow arguments]


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
for this is so that regular expressions do not have to account for the read within the name.
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

    Echo exceptions immediately as they occur.

`-c - -checksums`

    Set the level of ruffus checksums.

.. _getting_started-Building-reports:


Building tRNAnalysis reports
============================

Reports are generated using the following command once a the `full` command has completed::

    tranalysis make build_report


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
which the error occurred and restart the pipeline. Processing should
resume at the appropriate point.

.. note::

   Look out for upstream errors. For example, you may find that
   if the pipeline errors and stops, it may create the file and
   when the pipeline is started again, it will move to the next
   function, despite the previous file being empty. To fix this, delete the files
   created by the last task ran before restarting the pipeline.

Common errors
-------------

One of the most common errors when running the tRNAnalysis is::

    GLOBAL_SESSION = drmaa.Session()
    NameError: name 'drmaa' is not defined

This error occurs because you are not connected to the cluster. Alternatively
you can run the pipeline in local mode by adding `- -no-cluster` as a command line option.



.. _pipelineReporting:
