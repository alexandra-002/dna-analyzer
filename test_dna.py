from dna import validate_sequence, calculate_gc_content, count_bases


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