from dna import validate_sequence, calculate_gc_content, count_bases, read_fasta, analyze_sequences, read_fasta


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
    sequences = read_fasta("sample.fasta")

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