import sys, os, re

folder = sys.argv[1]
enz1 = sys.argv[2]
enz2 = sys.argv[3]

def enz_cut_site(enz):
    enz_list = enz.split('/')
    enzlen1 = len(enz_list[0])
    enzlen2 = len(enz_list[1])

    if enzlen1 > enz1len2:
        enz_1 = enz_list[0]
        enz_2 = enz.replace('/','')[enzlen2:]
    else:
        enz_2 = enz_list[1]
        enz_1 = enz.replace('/','')[:-enzlen1]
    return enz_1,enz_2
# find enzyme detection site
enz1_1,enz1_2 = enz_cut_site(enz1)
enz2_1,enz2_2 = enz_cut_site(enz2)

my_regex = r'^[ATGC]*'+enz1_1+r'$|^[ATGC]*'+enz2_1+r'$|^'+enz1_2+r'[ATGC]*$|^'+enz2_2+r'[ATGC]*$'

def make_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[:14] == 'rm_redundancy_':
            if input_file[-6:] == '.fastq':
                file_list.append(input_file)
    return file_list
#make file list
file_list = make_file_list(folder)

for each_file in file_list:
    with open(folder + each_file,'r') as f:
        print each_file +' is now processed ...'
        linecount = 0
        name = ''
        uniq_dict = {}
        for line in f:
            tmp = line.strip()
            if name == '': # tmp is name
                name = tmp
            else:          # tmp is sequence
                uniq_dict[tmp] = name
                name = ''
                linecount += 1
                if linecount % 100000 == 0:
                    print linecount
        keylist = uniq_dict.keys()        

        r = re.compile(my_regex)
        
        select = filter(r.match, keylist)
        select.sort()
        sel_file = open(each_file.replace('rm_redundancy','selected'),'w')
        check = 0
        for seq in select:
            sel_file.write('>'+uniq_dict[seq] + '\n' + seq + '\n')
