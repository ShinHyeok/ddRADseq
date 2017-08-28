

1. read quality check

*code
perl ngsShoRT.pl -pe1 <forward_sequence> -pe2 <backward_sequence> -o ../trim/<folder> -methods lqr -lqs 4 -lqp 50(recommanded) -t <cpu_num>

*setting
sudo perl -MCPAN - shell
<perl code> -- installing packages
  install String::Approx
  install PerlIO::gzip

input file : raw_file_folder/*.fastq
output file : trimmed_*.fastq


2. frequency test

## cutsite 나오면, 그 뒤 10bp 이용해서 

3. remove_redundancy

4. enzyme_site_selection

5. cat이용, R1,R2 merge (code같고, 69 80의 bp차이로 구분 가능)

6. ./usearch10.0.240_i86linux32 -id 0.9 -cluster_fast merge001.fasta  -uc 001.uc

7. arrange

8. cat이용, 모든 arranged file merge

9. 다시 usearch로 cluster를 찾는다.
