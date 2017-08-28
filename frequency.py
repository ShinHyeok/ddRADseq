import sys, os, re

folder = sys.argv[1]
bp = sys.argv[2]

def selected_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[-6:] == '.fastq':
            file_list.append(input_file)
    return file_list
# create fastq file list in selected folder
file_list = selected_file_list(folder)

frequency = {}

for afile in file_list:
    with open(folder+afile,'r') as f:
        line_count = 0
        target = 100000
        selectcount = 1
        for line in f:
            #header
            if selectcount == 1:
                line_count += 1
                if line_count == target:
                    #print line_count 
                    target += 100000
                header = re.split('@|:|_|/| |\n',line)
                name = header[1]
                selectcount += 1

            #sequence
            elif selectcount == 2:
                selectcount +=1
                l = line.strip()
                for i in range(len(l)-bp+1):
                    tmp_seq = l[i:i+bp]
                    if tmp_seq in frequency:
                        frequency[tmp_seq] += 1
                    else:
                        frequency[tmp_seq] = 1

            #qual_header
            elif selectcount == 3:
                selectcount +=1
                
            elif selectcount == 4:
                selectcount = 1
                

w = open('frequency.txt', 'w')
# only print frequency more than 100000
for k,v in frequency.items():
    if v > 9999:
        w.write(k+'\t'+v+'\n')
