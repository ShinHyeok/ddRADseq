import sys,re,os

def selected_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[-3:] == '.uc':
            file_list.append(input_file)
    return file_list

file_list = selected_file_list('./')

                
for thefile in file_list:
    if not thefile[3] == 't':
        continue
    print thefile
    w = open('rm_singlebatch_'+thefile.replace('uc','fasta'), 'w')
    
    with open(thefile,'r') as f:
        arrange = {}
        code = thefile[:3]
        for line in sorted(f):
            if line.startswith('H'):
                items = line.split()
                cluster = items[1]
                identitiy = items[3]
                name = items[8]
                std = items[9]
                if cluster in arrange:
                    arrange[cluster].append(name)
                else:
                    arrange[cluster] = [std,name]


        with open('selected_R1_'+code+'.fastq') as f1:
            table = {}
            for line in f1:
                if line.startswith('>'):
                    target = line.strip()[1:]
                else:
                    seq = line.strip()
                    table[target] = seq
            with open('selected_R2_'+code+'.fastq') as f2:
                for line in f2:
                    if line.startswith('>'):
                        target = line.strip()[1:]
                    else:
                        seq = line.strip()
                        table[target] = seq
                        
        i = 0
        values = arrange.values()
        for each in arrange.values():
            if len(each)<3:
                for name in each:
                    w.write('>'+name+'\n'+table[name]+'\n')
