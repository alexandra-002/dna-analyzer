from pathlib import Path
from src.dna import validate_sequence, calculate_gc_content, count_bases, read_fasta, analyze_sequences

def test_valid_sequence():
    assert validate_sequence("ATCG") == True


def test_invalid_sequence():
    assert validate_sequence("ATXYZ") == False


def test_gc_content():
    assert calculate_gc_content("GGCCAA") == 66.67


def test_base_count():
    counts = count_bases("AATCG")

    assert counts["A"] == 2
    assert counts["T"] == 1
    assert counts["C"] == 1
    assert counts["G"] == 1

def test_read_fasta():
    fasta_file = Path(__file__).parent.parent / "data" / "sample.fasta"

    sequences = read_fasta(fasta_file)

    assert sequences["gene_1"] == "ATCGATCGATCG"
    assert sequences["gene_2"] == "GGGCCCAAATTT"

def test_analyze_sequence_length():

    sequences = {
        "gene_test": "ATCG"
    }

    results = analyze_sequences(sequences)

    assert results["gene_test"]["length"] == 4

def test_missing_file():

    sequences = read_fasta("does_not_exist.fasta")

    assert sequences == {}

def test_empty_sequence():
    assert validate_sequence("") == False

def test_empty_fasta_file():
    sequences = read_fasta("empty.fasta")

    assert sequences == {}

def test_multiple_sequences():

    sequences = {
        "gene1": "ATCG",
        "gene2": "GGGG"
    }

    results = analyze_sequences(sequences)

    assert results["gene1"]["length"] == 4
    assert results["gene2"]["gc_content"] == 100.0

def test_lowercase_sequence():
    assert validate_sequence("atcg") == True