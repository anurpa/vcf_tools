#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Pavana Anur"
__date__="4 June 2021"

"""
Variant annotation tool. 

Given a VCF file, outputs annotated text file.

Usage example in a terminal: 
python vcf_process.py -v Challenge_data.vcf -o challenge_data_annotated.txt 

"""

import argparse
import json
import requests
import pandas as pd

def vcf_annot(args):
    """
    This functions takes VCF file as input and outputs annotated variants into a text file.
    Args:
        v: VCF file name
        o: Output file name
    Returns:
        Tab delimited text file with variant annotations.
    """
    
    headers=['chrom','pos','id','ref','alt','type','depth','alt_reads','alt_reads_percentage','ref_reads_percentage',\
             'allele_freq','symbol','major_consequence','gene_id_ens']
             
	#Initiate dataframe
    annot_df=pd.DataFrame(columns=headers)
    
    try:
        vcf_input=open(args.v,'r')
            
    # If file not found, exit script
    except FileNotFoundError:
        print ("File not found. Check file name and path.")
        return
    
    
    for line in vcf_input:
        line=line.strip()

        #Skip metainformation lines
        if not line.startswith("#"):
            line_split=line.split("\t")
            #assign values to variables
            chrom=line_split[0]
            pos=line_split[1]
            var_id=line_split[2]
            ref_base=line_split[3]
            alt_base=line_split[4]

            #Get type from info field, to determine most deleterious additional info is needed. 
            info=line_split[7].split(";")
            info_dict=dict([field.split("=") for field in info])
            var_type=info_dict['TYPE']

            #Get depth of sequence coverage 
            var_depth=info_dict['DP']

            #Get number of reads supporting the variant
            var_reads=info_dict['AO']

            #Calculate percentage of reads supporting the variant 
            #Based on number of alternate alleles, counts are given for each alt allele
            #For total reads supporting variant, add all counts 
            var_reads_total=sum(float(count) for count in info_dict['AO'].split(","))

            try:
                var_percent=round(var_reads_total/float(info_dict["DP"])*100,2)

            except:
                var_percent="na"

            #Calculate percentage of reads supporting the reference 
            try:
                ref_percent=round(float(info_dict['RO'])/float(info_dict["DP"])*100,2)

            except:
                ref_percent="na"


            #Get annotations from Exac
            try:
                get_url=("http://exac.hms.harvard.edu/rest/variant/variant/{0}-{1}-{2}-{3}".format(chrom,pos,ref_base,alt_base))
                get_data = requests.get(get_url)

                #Convert data to json format
                data_json=get_data.json()

                #assign data to variables
                allele_freq=round(data_json["allele_freq"], 6)
                symbol=data_json["vep_annotations"][0]["SYMBOL"]
                major_consequence=data_json["vep_annotations"][0]["major_consequence"]
                gene=data_json["vep_annotations"][0]["Gene"]

            #When data not found
            except:
                allele_freq="na"
                symbol="na"
                major_consequence="na"
                gene="na"

            annot_df.loc[len(annot_df)]=[chrom,pos,var_id,ref_base,alt_base,var_type,var_depth,var_reads,var_percent,\
                                        ref_percent,allele_freq,symbol,major_consequence,gene]
            
            

    vcf_input.close()    
    
    #Write data frame to file 
    annot_df.to_csv(args.o,sep="\t",index=False)
    
    
    
#To parse arguments from command line
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v",action="store",dest="v", help="VCF file to be annotated",required=True)
    parser.add_argument("-o",action="store",dest="o", help="output file name")
    args = parser.parse_args()  
    vcf_annot(args) 