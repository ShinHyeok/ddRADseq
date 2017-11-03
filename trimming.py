import os,re,sys


directory = sys.argv[1]
def selected_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[:3] == 'raw':
            file_list.append(input_file)
    return file_list

file_list = selected_file_list(directory)
#Make string list with files straring with raw in selected directory

for thefile in file_list:
    linecount = 1
    print 'processing '+ thefile +' ...'
    w = open(directory+thefile.replace('raw','trimmed'),'w')
    #Trimmed file is generated in same directory
    with open(directory+thefile,'r') as f:
        for line in f:
            if linecount == 1: #seq name is recorded
                seq_name = line.strip()
                linecount += 1
            elif linecount == 2: #read sequence
                seq = line.strip()
                linecount += 1
            elif linecount == 3: #+
                linecount += 1
                continue
            else: #Quality is recorded as phred33 score
                quality = line.strip()
                len_qual = len(quality)
                board = 0
                for base_qual in range(len_qual): #Check every base
                    if ord(tmp_qual) < 53: #How many base has low quality is recorded. Standard is 20(1% error rate)
                        board += 1
                if not board*2 >= len_qual: #More than half of sequence must have score higher than 20
                    w.write(seq_name+'\n'+seq+'\n'+'+\n'+quality+'\n')
                linecount = 1
print 'done'
