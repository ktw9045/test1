import sys

print(sys.argv)

name = sys.argv[1]

print("Hello %s"%name)

import sys

#print(sys.argv)

sample = sys.argv[1]

print("bwa mem"+sample+"_1.fastq.gz "+sample+"_2.fastq.gz")
print("picard MarkDuplicate "+sample+".bam")
