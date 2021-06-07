# VCF Annotation Tools

This repository contains tools for annotating a VCF file. 
Given a VCF file as input to  vcf_process.py, output of annotated VCF file is generated.

More information on a VCF file format can be found [here](https://samtools.github.io/hts-specs/VCFv4.2.pdf).

## Table of Contents
* [Build](#build)
* [Prerequisites](#requirements)
* [Running VCF annotation tool](#running)
* [Description of output file](#output)
* [Future additions](#additions)

## <a name="build">Build</a>
* Tool was built using:
    * Python 3.7.7 
    * Conda 4.9.2
    
## <a name="requirements">Prerequisites</a>
* To run this tool, require:
    * Python 3.7.7
    * Python libraries: argparse, json, pandas, requests

## <a name="running">Running</a>
For help on using this tool for annotation of VCF file run: 
```
python vcf_process.py -h 
```

Usage example:

```
python vcf_process.py -v Challenge_data.vcf -o challenge_data_annotated.txt 
```

## <a name="output">Description of output file</a>

The following columns are available in annotated output file: 

Column|Description
------|-----------
chrom| The chromosome number of the variant.
pos| Position on the chromosome of the variant.
id| Unique identifier of variant if available.(eg: dbSNP id)
ref| Reference base.
alt| Alternate base.
depth| Depth of sequence coverage at the site of variation.
alt_reads| Number of reads supporting the variant.
alt_reads_percentage| Percentage of reads supporting the variant.
ref_reads_percentage| Percentage of reads supporting the reference.
allele_freq| Allele frequency of variant from [ExAC API](http://exac.hms.harvard.edu/)
symbol| HGNC gene symbol.
major_consequence| Major consequence on the variant from [ExAC API](http://exac.hms.harvard.edu/), based on VEP annotation.
gene_id_ens| Ensembl gene ID, obtained from [ExAC API](http://exac.hms.harvard.edu/)

Example of output file: challenge_data_annotated.tsv

## <a name="additions">Future additions</a>
* This tool can be further edited to add:
   * Additional annotations 
   *  Extract genotype information
   *  Filtering variants
      

