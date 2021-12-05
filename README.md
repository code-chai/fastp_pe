# Hello!
We're going to run `fastp` to trim any adaptors and filter any low quality reads.
While I understand it's possible to run a process on all files in a directory using wildcards like so:
```{sh}
fastp -i ./*pass_1.fastq.gz #...
```
I'm not sure how to automatically make the output file names the same as the input file names, thus this script was needed! 
I believe **this** might be a way : https://itectec.com/unixlinux/bash-how-to-write-output-to-a-file-of-the-same-name-as-the-input/ but for want of time I'm going with python. 

We can run `BWA` later in paired end read mode, so we won't merge reads.
Make sure to **place yourself in the folder with all your gzipped fastq paired end reads first.** 
Also, **make a folder called fastp inside that folder**.
I could probably tell python to make it for you, but let's meet eachother halfway!
.°(ಗдಗ。)°.

I heavily referenced the approach of Erick Lu (https://erilu.github.io/python-fastq-downloader/#automating-downloads-using-python). 
I would also refer to the link if you want to try using python to automate getting data from SRA.

Dependencies: 
- Python and modules `os` and `subprocess`
- fastp
- multiqc

*Have fun!*