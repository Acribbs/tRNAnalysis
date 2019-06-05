"""trna_fragment_bed.py - generate a bed file from a fasta file of tRNA sequences
=================================================================================

Purpose
-------
The aim of this script is to take a fasta file of clustered tRNAs and then output a
bed file of different tRNA fragments depending on the options given.

Current tRNA half features supported:
* tRH-5' - 1-33
* tRH-DA - 14-43
* tRH-DTA - 17-54
* tRH-AT - 38-69
* tRH-3' - 43-73

Current tRNA fragment features supported:
* tRF-5' - 1-15
* tRF-3' - 58-73
* tRF-D - 8-23
* tRF-DA - 20-35
* tRF-A - 27-42
* tRF-AT - 33-53
* tRF-T - 45-71


Usage
-----
python /ifs/devel/adamc/tRNAnalysis/trnanalysis/python/trna_fragment_bed.py -I hg38_clusterInfo.fa -S test.bed

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

    outfile = IOTools.open_file(options.stdout.name, "w")
    trna_options = ["tRH-5'","tRH-DA","tRH-DTA","tRH-AT","tRH-3'","tRF-5'", "tRF-3'", "tRF-D", "tRF-DA", "tRF-A", "tRF-AT", "tRF-T"]
    for trna in trna_options:
        infile = IOTools.open_file(options.stdin.name)
        iterator = FastaIterator.FastaIterator(infile)

        

        d = collections.OrderedDict()
        cluster_dict = dict()

        # first iterate over the fasta file
    
        for cur_record in iterator:
            
            title = cur_record.title
            m = re.match("(cluster\d+):chr\S+.tRNA\d+-(\S+)-\((\S+)\)", title)

            cluster = m.group(1)
            trna_group = m.group(2)
            strand = m.group(3)

            chrom = cluster + ":" + trna_group + "-"
            score = "."
            print(trna)
            if trna == "tRH-5'":
                start = "1"
                end = "33"
            elif trna == "tRH-DA":
                start = "14"
                end = "43"
            elif trna == "tRH-DTA":
                start = "17"
                end = "54"
            elif trna == "tRH-AT":
                start = "38"
                end = "69"
            elif trna == "tRH-3'":
                start = "43"
                end = "73"
            elif trna == "tRF-5'":
                start = "1"
                end = "15"
            elif trna == "tRF-3'":
                start = "58"
                end = "73"
            elif trna == "tRF-D":
                start = "8"
                end = "23"
            elif trna == "tRF-DA":
                start = "20"
                end = "35"
            elif trna == "tRF-A":
                start = "27"
                end = "42"
            elif trna == "tRF-AT":
                start = "33"
                end = "53"
            elif trna == "tRF-T":
                start = "45"
                end = "71"
            else:
                print("tRNA fragment not implemented")
                break
            outfile.write(("%s\t%s\t%s\t%s\t%s\t%s\n")%(chrom, start, end, trna, score, strand))


    E.stop()

if __name__ == "__main__":
    sys.exit(main(sys.argv))
