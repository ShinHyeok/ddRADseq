import sys,re,os

criteria = sys.argv[1]
criteria = int(criteria)

index_seq = {}
with open('merged.fasta','r') as f:
    for line in f:
        if line.startswith('>'):
            index = line.strip()[1:]
        else:
            seq = line.strip()
            index_seq[index]=seq

arrange = {}
with open('results.uc','r') as f:
    for line in f:
        if line.startswith('H'):
            items = line.split()
            cluster = items[1]
            identitiy = items[3]
            name = items[8]
            std = items[9]
            if cluster in arrange:
                name_c = name+'_'+identitiy
                name_i = name_c.ljust(25)
                arrange[cluster].append(name_i)
            else:
                std_c = std+'_100.0'
                std_i = std_c.ljust(25)
                name_c = name+'_'+identitiy
                name_i = name_c.ljust(25)
                arrange[cluster] = [std_i,name_i]

                
                
w = open('arranged_cluster.txt', 'w')
for k,v in arrange.items():
    if len(v) > criteria-1:
        tmp_list = []
        new_value = []
        for read in v:
            fileindex = read.split('.')[0]
            tmp_list.append(fileindex)
        tmp_list = sorted(set(tmp_list))
        if len(tmp_list) < criteria:
            continue
        for read in v:
            seq_sel = read.split('_')[0]
            new_value.append(read + index_seq[seq_sel])
        w.write('cluster#'+k+'\n')
        new_value.sort()
        for nv in new_value:
            w.write(nv + '\n')
