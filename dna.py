
def validate_sequence(sequence):
    """
    Check whether a DNA sequence only contains A, T, C, G.
    """

    valid_bases = "ATCG"

    for base in sequence:
        if base not in valid_bases:
            return False

    return True


def count_bases(sequence):
    """
    Count each nucleotide in a DNA sequence.
    """

    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G")
    }

    return counts


def calculate_gc_content(sequence):
    """
    Calculate GC percentage.
    """

    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / len(sequence)) * 100

    return round(gc_content, 2)

def read_fasta(filename):
    """
    Read a FASTA file and return sequences as a dictionary.
    """

    sequences = {}

    with open(filename, "r") as file:
        sequence_name = None

        for line in file:
            line = line.strip()

            if line.startswith(">"):
                sequence_name = line[1:]
                sequences[sequence_name] = ""

            else:
                sequences[sequence_name] += line

    return sequences

def main():
    sequence = input("Enter a DNA sequence: ").upper()

    if len(sequence) == 0:
        print("Sequence cannot be empty")
        return

    if not validate_sequence(sequence):
        print("Invalid DNA sequence")
        return

    counts = count_bases(sequence)
    gc_content = calculate_gc_content(sequence)

    print("Sequence:", sequence)
    print("Length:", len(sequence))
    print("GC Content:", gc_content, "%")

    print("A:", counts["A"])
    print("T:", counts["T"])
    print("C:", counts["C"])
    print("G:", counts["G"])


if __name__ == "__main__":
    main()