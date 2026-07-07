
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

def analyze_sequences(sequences):
    """
    Analyze multiple DNA sequences.
    """

    results = {}

    for name, sequence in sequences.items():
        results[name] = {
            "length": len(sequence),
            "gc_content": calculate_gc_content(sequence),
            "counts": count_bases(sequence)
        }

    return results

def print_report(results):
    """
    Print analysis results.
    """

    for name, data in results.items():

        print("\nSequence:", name)
        print("Length:", data["length"])
        print("GC Content:", data["gc_content"], "%")

        print("A:", data["counts"]["A"])
        print("T:", data["counts"]["T"])
        print("C:", data["counts"]["C"])
        print("G:", data["counts"]["G"])

def main():
    sequences = read_fasta("sample.fasta")

    results = analyze_sequences(sequences)

    print_report(results)


if __name__ == "__main__":
    main()