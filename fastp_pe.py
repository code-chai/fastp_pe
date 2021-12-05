import subprocess 
import os

cwdfiles = []
try:
    for file in os.listdir(path='.'):
        if file.endswith('.fastq.gz'):
            cwdfiles.append(file)
    cwdfiles = sorted(cwdfiles)
except KeyboardInterrupt:
    exit()

for i in range(0,len(cwdfiles),2):
    uno = cwdfiles[i]
    dos = cwdfiles[i+1]
    #No, I can't speak spanish. 
    print(f'Generating QC\'ed fastq\'s for: {uno[0:10]}')
    fastp = f'fastp -i {uno[:-9]}.fastq.gz -I {dos[:-9]}.fastq.gz \
        -o fastp/{uno[:-9]}.fastq -O fastp/{dos[:-9]}.fastq \
        --cut_tail --correction \
        --unpaired1 fastp/{uno[:-9]}.fastq.gz --unpaired2 fastp/{dos[:-9]}.fastq.gz \
        --json fastp/{uno[0:10]}_fastp.json --html fastp/{uno[0:10]}_fastp.html'
        #I believe you need `fastp.extension` on the end of report files to be found by multiqc 
#Since I'm eventually going to unzip the fastq files, I'm not going to gzip the output.
#I'll definitely free up some storage later, yeah...
    print(f'Command used was: {fastp}')
    subprocess.call(fastp, shell = True)

#Now let's summarise the bunch! 
subprocess.call('multiqc .', shell = True)
#The output "multiqc_report.html" can be viewed from your browser.

