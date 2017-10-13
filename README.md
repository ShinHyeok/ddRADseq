

# 1. read quality check

\*code

perl ngsShoRT.pl -pe1 <forward_sequence> -pe2 <backward_sequence> -o ../trim/<folder> -methods lqr -lqs 4 -lqp 50(recommanded) -t <cpu_num>

\*setting  
sudo perl -MCPAN - shell  
(perl code- to install packages)  
  install String::Approx  
  install PerlIO::gzip  

input file : raw_file_folder/$.fastq  
output file : trimmed_$.fastq


# 2. frequency test

\*code  
python frequency.py <folder> <bp>  
  ex) python frequency.py 'trimmed_raw/r2/' 6  

input file : $.fastq  
output file : frequency.txt


# 3. remove_redundancy

\*code  
python remove_redundancy.py <folder>  
  
input file : trimmed_$.fastq  
output file : rm_redundancy_$.fastq


# 4. enzyme_site_selection

\*code  
python enzyme_site_selection.py <folder> <enz1seq> <enz2seq>  
  ex) python enzyme_site_selection.py rm_redundancy/ CCTGCA/GG GC/GGCCGC  
  
 input file : rm_redundancy_$.fastq  
 output file : selected_$.fastq


# 5. by using cat, R1,R2 merge (if exist)

\*code  
cat selected_$<>.fastq > merged<>.fastq  
merge every file
  ex) cat selected_\*001.fastq > merged001.fasta  
      cat selected_\*002.fastq > merged002.fasta  
      .....  
input file : selected_$<>.fastq  
output file : merged<>.fastq  


# 6. making cluster using usearch (each file)

\*code  
./usearch10.0.240_i86linux32 -id 0.9 -cluster_fast merge<>.fasta  -uc <>.uc  
  ex) ./usearch10.0.240_i86linux32 -id 0.9 -cluster_fast merge001.fasta  -uc 001.uc  
make cluster of every file.

input : merged<>.fastq  
output : <>.uc

# 7. remove useless reads
some reads has variable pattern in single sample so we can't use those reads to analyze

\*code  
python rm_single_batch.py  

input : <>.uc, selected_$.fastq  
output : rm_singlebatch_<>.fasta

# 8. by using cat, merge every files to make cluster

\*code  
cat rm_singlebatch\* > merged.fasta

input : rm_singlebatch_<>.fasta  
output : merged.fasta

# 9. Again, make cluster by using usearch

\*code  
./usearch10.0.240_i86linux32 -id 0.9 -cluster_fast merged.fasta  -uc results.uc  


input : merged.fasta  
output : results.uc

# 10. arrange results, select cluster

\*code  
python arrange_result.py <standard_number>  
  ex) python arrange_result.py 6 
  #which mean only collect information having sequence of at least 6 sample

input : merged.fasta, results.uc  
output : arranged_cluster.txt

# 11. clean up cluster

\*code  
python 1by1_matching.py

input : arranged_cluster.txt
output : cleared_cluster.txt

Version 0.2
2017.09.01
