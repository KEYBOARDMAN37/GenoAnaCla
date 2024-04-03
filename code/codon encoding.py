import os
from collections import Counter


def remove_non_standard_symbols(dataset):
    valid_symbols = {'A', 'C', 'G', 'T'}
    cleaned_dataset = []
    for sequence in dataset:
        cleaned_sequence = ''.join(symbol for symbol in sequence if symbol in valid_symbols)
        cleaned_dataset.append(cleaned_sequence)
    return cleaned_dataset
# Function to count the frequencies of all 64 codons

def count_codon_frequencies(encoded_dataset):
    # Flatten the list of encoded sequences
    all_codons = [codon for sequence in encoded_dataset for codon in sequence]
    # Count the frequencies of all 64 codons
    codon_frequencies = Counter(all_codons)
    # Sort the codon frequencies in descending order
    sorted_codon_frequencies = dict(sorted(codon_frequencies.items(), key=lambda item: item[1], reverse=True))
    return sorted_codon_frequencies

def encode_genome_sequences(dataset):
    codon_encoding = {
        'AAA': 1, 'AAC': 2, 'AAG': 3, 'AAT': 4,
        'ACA': 5, 'ACC': 6, 'ACG': 7, 'ACT': 8,
        'AGA': 9, 'AGC': 10, 'AGG': 11, 'AGT': 12,
        'ATA': 13, 'ATC': 14, 'ATG': 15, 'ATT': 16,
        'CAA': 17, 'CAC': 18, 'CAG': 19, 'CAT': 20,
        'CCA': 21, 'CCC': 22, 'CCG': 23, 'CCT': 24,
        'CGA': 25, 'CGC': 26, 'CGG': 27, 'CGT': 28,
        'CTA': 29, 'CTC': 30, 'CTG': 31, 'CTT': 32,
        'GAA': 33, 'GAC': 34, 'GAG': 35, 'GAT': 36,
        'GCA': 37, 'GCC': 38, 'GCG': 39, 'GCT': 40,
        'GGA': 41, 'GGC': 42, 'GGG': 43, 'GGT': 44,
        'GTA': 45, 'GTC': 46, 'GTG': 47, 'GTT': 48,
        'TAA': 49, 'TAC': 50, 'TAG': 51, 'TAT': 52,
        'TCA': 53, 'TCC': 54, 'TCG': 55, 'TCT': 56,
        'TGA': 57, 'TGC': 58, 'TGG': 59, 'TGT': 60,
        'TTA': 61, 'TTC': 62, 'TTG': 63, 'TTT': 64
    }

    encoded_dataset = []
    for sequence in dataset:
        encoded_sequence = []
        for i in range(0, len(sequence), 3):
            codon = sequence[i:i+3]
            if len(codon) == 3:
                encoded_sequence.append(codon_encoding.get(codon, 0))
        encoded_dataset.append(encoded_sequence)
    return encoded_dataset

# Input folder path
input_folder = "virus_sequenceonlynucleotide/"

# Output folder path
output_folder = "codonfolder/"

# Get the list of files in the input folder
input_files = os.listdir(input_folder)

for input_file in input_files:
    # Input file path
    input_file_path = os.path.join(input_folder, input_file)

    # Read the content from the input file
    with open(input_file_path, 'r') as f:
        genome_dataset = f.readlines()

    # Process the genome dataset
    cleaned_dataset = remove_non_standard_symbols(genome_dataset)
    encoded_dataset = encode_genome_sequences(cleaned_dataset)

    # Output file path
    output_file_path = os.path.join(output_folder, input_file)

    for input_file in input_files:
        # ... (existing code for reading the input file and processing the dataset)

        # Count the frequencies of all 64 codons
        codon_frequencies = count_codon_frequencies(encoded_dataset)

        # Output file path for codon frequencies
        output_freq_file_path = os.path.join(output_folder, f"codon_frequencies_{input_file}")

        # Write the codon frequencies to the output file in descending order
        with open(output_freq_file_path, 'w') as freq_file:
            for codon, frequency in codon_frequencies.items():
                freq_file.write(f"{codon}: {frequency}\n")

    # Write the encoded dataset to the output file
    with open(output_file_path, 'w') as file:
        for sequence in encoded_dataset:
            encoded_sequence = ' '.join(str(code) for code in sequence)
            #encoded_sequence += ' -1 -2'
            file.write(encoded_sequence + '\n')
           # print(encoded_sequence)