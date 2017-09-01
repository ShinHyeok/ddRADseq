import sys,re,os

tmp_dict = {}
with open('arranged_cluster.txt.txt','r') as f:
    writing = open('cleared_cluster.txt','w')
    for line in f:
        #third, after save all of cluster information
        if line.startswith('cluster'):
            if not len(tmp_dict.keys()) == 0:
                #base on matching %, arrange seq
                per = []
                for key in tmp_dict.keys():
                    percent = key.split('_')[1]
                    per.append(percent)
                new_key = [x for _,x in sorted(zip(per,tmp_dict.keys()))]
                
                writing.write(cluster+'\n')
                check = 1
                for k in new_key:
                    k_i = k.ljust(40)
                    v = tmp_dict[k]
                    #standard sequence is always saved first
                    if check == 1:
                        std = v
                        writing.write(k_i+v+'\n')
                        check = 0
                    else: #test sequence one by one to the sequence of standard
                        tmp_seq = ''
                        for a in range(len(std)):
                            if len(v)<= a:
                                tmp_seq += '-'
                                continue
                            else: #if seq is same as the one from standard, leave as blank
                                if v[a] == std[a]:
                                    tmp_seq += ' '
                                else:
                                    tmp_seq += v[a]
                        writing.write(k_i+tmp_seq+'\n')
            #first, save cluster name
            cluster = line.strip()
            tmp_dict = {}
        else: #second, each sequence is added to dictionary
            name,seq = line.split()
            tmp_dict[name] = seq
