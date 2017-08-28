

# 1. read quality check

\*code

perl ngsShoRT.pl -pe1 <forward_sequence> -pe2 <backward_sequence> -o ../trim/<folder> -methods lqr -lqs 4 -lqp 50(recommanded) -t <cpu_num>

\*setting  
sudo perl -MCPAN - shell  
perl code-installing packages  
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
and reapeat to every file  
  ex) cat selected_\*001.fastq > merged001.fasta  
      cat selected_\*002.fastq > merged002.fasta  
      .....  
input file : selected_*<>.fastq  
output file : merged<>.fastq  


# 6. making cluster using usearch (each file)

\*code  
./usearch10.0.240_i86linux32 -id 0.9 -cluster_fast merge<>.fasta  -uc <>.uc  
  ex) ./usearch10.0.240_i86linux32 -id 0.9 -cluster_fast merge001.fasta  -uc 001.uc  


7. arrange

8. cat이용, 모든 arranged file merge

9. 다시 usearch로 cluster를 찾는다.
