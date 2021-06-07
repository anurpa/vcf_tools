# VCF Annotation Tools

This srepository contains tools for annotating a VCF file. 
Given a VCF file as input to  vcf_process.py, output of annotated VCF file is generated.

More information a VCF file format can be found [here](https://samtools.github.io/hts-specs/VCFv4.2.pdf).

## Table of Contents
* [Build](#build)
* [Requirements](#requirements)
* [Running VCF annotation tool](#running)

## <a name="build">Build</a>
* Tool was built using:
    * Python 3.7.7 
    * Conda 4.9.2
    
## <a name="requirements">Requirements</a>
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
