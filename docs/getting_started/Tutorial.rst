.. _getting_started-Tutorial:


==============================
Running tRNAnalysis - Tutorial
==============================


Before beginning this tutorial make sure you have tRNAnalysis installed correctly,
please see here (see :ref:`getting_started-Installation`) for installation instructions.

In the following section we will run a toy example pipeline that demonstrates the functionality
of tRNAnalysis. tRNAnalysis can be run locally or distributed across a cluster. 
This tutorial will explain the steps required to run tRNAnalysis.

Tutorial start
--------------

**1.** First download the tutorial data::

   wget https://www.cgat.org/downloads/public/adam/trnanalysis/test_trna.tar.gz
   tar -zxvf test_trna.tar.gz


**2.** Next we will generate a configuration yml file so the pipeline output can be modified::

   cd test_trna
   trnanalysis trna config

This will generate a **pipeline.yml** file containing the configuration parameters than can be used to modify
the output of the pipleine. However, for this tutorial you do not need to modify the parameters to run the 
pipeline. In the :ref:`modify_config` section below I have detailed how you can modify the config file to
change the output of the pipeline.

.. note::

   There is already a pipeline.yml file within the test data so you dont really need to run the command above this time.

**3.** Next we will run the pipeline::

   trnanalysis trna make full -v5 --no-cluster

This ``--no-cluster`` will run the pipeline locally if you do not have access to a cluster. Alternatively if you have a
cluster remove the ``--no-cluster`` option and the pipleine will distribute your jobs accross the cluster. For information on how to configure your cluster please see the `cluster config help <https://trnanalysis.readthedocs.io/en/latest/getting_started/Cluster_config.html>`_.

.. note::

   There are many commandline options available to run the pipeline. To see available options please run :code:`trnanalysis --help`.


The pipeline is mostly quite quick to execute. However, it can take a considerable time to generate the bowtie indexes, in the future we will parameterise this so you can use pre-configured bowtie indexes so these do not have to keep being generated each time the pipeline is ran.

**4.** Generate a report

The final step is to generate a report to display the output of the tRNAnalysis. 
In order to generate these reports run the command::

    trnanalysis trna make build_report -v 5 --no-cluster

This will generate a MultiQC report in the folder `MultiQC_report.dir/` and an Rmarkdown report in `R_report.dir/Final_report/index.html`. 


This completes the tutorial for running the tRNAnalysis , hope you find it as useful as we do for analysing tRNA sequencing data. 
