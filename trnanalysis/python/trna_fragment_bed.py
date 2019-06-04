"""trna_fragment_bed.py - generate a bed file from a fasta file of tRNA sequences
=================================================================================

Purpose
-------
The aim of this script is to take a fasta file of clustered tRNAs and then output a
bed file of different tRNA fragments depending on the options given.

Current tRNA fragment features supported:
* tRH-5' - 1-33
* tRH-DA - 14-43
* tRH-DTA - 17-54
* tRH-AT - 38-69
* tRH-3' - 43-73

* tRF-5' - 1-15
* tRF-3' - 58-73


Usage
-----


Options
-------

-t, --trna-scheme
    Name of the tRNA scheme that a bed file is required to make


Type::

   python trna_fragment_bed.py --help

for command line help.

Command line options
--------------------

"""

import sys
import re
import cgat.FastaIterator as FastaIterator
import cgatcore.iotools as IOTools
import cgatcore.experiment as E
import collections

def main(argv=None):
    """script main.

    parses command line options in sys.argv, unless *argv* is given.
    """

    if not argv:
        argv = sys.argv

    # setup command line parser
    parser = E.OptionParser(
        version="%prog version: $Id$", usage=globals()["__doc__"])

    parser.add_option(
        "--trna-scheme", dest="trna_scheme", type="choice",
        choices=("tDR-5'", "tRH-DA"),
        help="name of the tRNA scheme to make bed file for[default=%default]")

    parser.set_defaults(
        trna_scheme=None
    )

    (options, args) = E.start(parser, argv=argv)

    if len(args) == 0:
        args.append("-")

    E.info(options.stdin)


    infile = IOTools.open_file(options.stdin.name)
    iterator = FastaIterator.FastaIterator(infile)

    outfile_info = IOTools.open_file(options.stdout.name, "w")

    d = collections.OrderedDict()
    cluster_dict = dict()

    # first iterate over the fasta file
    for cur_record in iterator:
        
        title = cur_record.title
        m = re.match("(cluster\d+):chr\S+.tRNA\d+-(\S+)-\((\S+)\)", title)

        cluster = m.group(1)
        print(cluster)
        trna = m.group(2)
        strand = m.group(3)

        chrom = cluster + ":" + trna + "-"
        score = "."

        if options.trna_scheme == "tDR-5'":
            start = "1"
            end = "33"
        else:
            start = ""
            end = ""

        options.stdout.write(("%s\t%s\t%s\t%s\t%s\t%s\n")%(chrom, start, end, options.trna_scheme, score, strand))


    E.stop()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
