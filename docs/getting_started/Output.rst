.. _tRNAnalysis-report:

======================
The tRNAnalysis report
======================

Before running the report
-------------------------

For the report to run successfully you will need to set up a design file (Actually,
you can have multiple design files in there and all will run simultaneously)
that controls how the differential expression model and contract will be
performed.

The file has the naming convention design_<test>_<control>_<test>_<column>.csv

* `<test>` - refers to the test that you plan to run. There are two options "ltr" or "wald".
* `<control>` - This is the name of your control condition i.e. the samples you want to test against. This should match on of the samples in the <column> of the file.
* `<test>` - This is the name of the test condition. This should match with one of the samples in the <column> of the file
* `<column>` - This is a column that you want to use for your testing in the design_* file

tRNAnalysis runs DEseq2 under the hood so you can refer to the bioconductor help
pages for further information on how to set up contrasts for your data.

The design file should be laid out as follows, with the last model column
detailing the model that you would like DESeq2 to run for the data:

.. csv-table:: design layout
   :file: https://www.cgat.org/downloads/public/adam/trnanalysis/design_wald_plac_k10_condition.csv
   :widths: 30, 70
   :header-rows: 1


Opening the report
------------------

Once you have ran the software with the command::

  trnanalysis trna make full

and::

  trnanalysis trna make build_report

a final html report should have been generated.

In order to access this report please open the file called FinalReport.html
which will be located within the directory that you ran tRNAnalysis. This
should open the report in your preferred browser.

Understanding the report
------------------------

The report contains a number of tabs at the top that display the analysis
performed when the pipeline was ran. All of the report is annotated, which
should make understanding the report output easier. However, if there are
sections that you feel could be explained better then please raise an `issue <https://github.com/Acribbs/tRNAnalysis/issues>`_
on github.
