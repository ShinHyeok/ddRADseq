import sys, os, re

folder = sys.argv[1]

def selected_file_list(input_dir):
    file_list = []
    input_file_list = os.listdir(input_dir)
    for input_file in input_file_list:
        if input_file[-6:] == '.fastq':
            if input_file[:8] == 'trimmed_':
                file_list.append(input_file)
    return file_list
    
# create fastq file list in selected folder
file_list = selected_file_list(folder)

frequency = {}

for afile in file_list:
    with open(afile,'r') as f:
        line_count = 0
        target = 100000
        selectcount = 1
        header_seq = {}
        writing = open('rm_redundancy_'+afile.replace('trimmed_',''), 'w')
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
                if l not in header_seq: # if seq is already uploaded to dictionary, it will be removed
                    header_seq[l] = name

            #qual_header
            elif selectcount == 3:
                selectcount +=1
                
            elif selectcount == 4:
                selectcount = 1
                
            
        ordered = header_seq.keys()
        ordered.sort()
        for t in ordered:
            writing.write(header_seq[t] + '\n' + t + '\n')
