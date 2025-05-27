import pandas as pd
from Bio import SeqIO


def preprocess_data(file, threshold=0.5):
    # CSV
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        records = [r for r in SeqIO.parse(file, 'fastq')
                   if min(r.letter_annotations['phred_quality']) >= threshold * 40]
        df = pd.DataFrame({'id': [r.id for r in records],
                           'sequence': [str(r.seq) for r in records]})
    return df
