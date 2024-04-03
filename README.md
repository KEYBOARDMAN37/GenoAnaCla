# GenoAnaCla (Genome Analyzer and Classifier)
There are three folders: (1) AccessionID, (2) code and (3) preprocessed abstracted genome sequences. 

(1)AccessionID folder contains the Genbank’s ID of collected genome sequences of 15 RNA viruses. Genome sequences were downloaded in three forms (Nucleotide, Coding Region and Protein). 

(2)Code folder contains two Python scripts. Original genome sequence in nucleotide form contains a definition line. In coding region and protein forms, a genome sequence may contain many definitions lines. 
(a)same_accesssion.py is used to preporocess the genome sequences in three forms. The script takes the original genome sequences  and removes the redundant information present in the genome sequences. The preprocessed sequences are stored in the preprocessed abstracted genome sequences folder.  
(b)codon encoding.py  This script takes preprocessed genome sequences in nucleotide form and then finds codons in each genome sequences of viruses, encode codons and also counts the total frequencies of codons in each virus genome sequence.

(3)Preprocessed abstracted genome sequences folder contains the preprocessed sequences data that are transformed into integers.  In nucleotide form, each line represents a genome sequence in one line, and for the other  two forms (coding region and protein), each line represents a coding region or a protein sequence. In codon, three nucleotides are changed into respective codon. !!! For this folder, we use Multi-part archive technique to compress the sequences, and when you download and extract the zip files, please make sure you download all series zip files. For example, when you want to extract Protein file, please extract Protein.zip, and make sure you also have Protein.z01, Protein.z02... and they are all in one same path.!!!

