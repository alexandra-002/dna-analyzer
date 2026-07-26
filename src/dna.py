
import argparse
import csv
from pathlib import Path


def validate_sequence(sequence):
    """
    Validate that a DNA sequence contains valid IUPAC nucleotide codes.

    Allows standard DNA bases and ambiguity codes.
    """

    if not sequence:
        return False

    sequence = sequence.upper()

    valid_bases = "ATCGNRYSWKMBDHV"

    return all(base in valid_bases for base in sequence)


def count_bases(sequence):
    """
    Count nucleotide frequencies in a DNA sequence.

    Args:
        sequence (str): DNA sequence.

    Returns:
        dict: Counts of A, T, C, and G.
    """

    sequence = sequence.upper()

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G")
    }


def calculate_gc_content(sequence):
    """
    Calculate GC percentage using only known DNA bases.
    Ambiguous bases are ignored.
    """

    sequence = sequence.upper()

    counts = count_bases(sequence)

    valid_length = (
        counts["A"]
        + counts["T"]
        + counts["C"]
        + counts["G"]
    )

    if valid_length == 0:
        return 0

    gc_content = (
        (counts["G"] + counts["C"]) / valid_length
    ) * 100

    return round(gc_content, 2)


def reverse_complement(sequence):
    """
    Return the reverse complement of a DNA sequence.

    Supports standard bases and IUPAC ambiguity codes.
    """

    sequence = sequence.upper()

    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",

        # IUPAC ambiguity codes
        "N": "N",
        "R": "Y",
        "Y": "R",
        "S": "S",
        "W": "W",
        "K": "M",
        "M": "K",
        "B": "V",
        "V": "B",
        "D": "H",
        "H": "D"
    }

    return "".join(
        complement[base]
        for base in reversed(sequence)
    )


def read_fasta(filename):
    """
    Read DNA sequences from a FASTA file.

    Args:
        filename (str or Path): FASTA file location.

    Returns:
        dict: Sequence names and sequences.
    """

    sequences = {}

    try:
        with open(filename, "r") as file:

            sequence_name = None

            for line in file:

                line = line.strip()

                if not line:
                    continue

                if line.startswith(">"):
                    sequence_name = line[1:].strip()
                    sequences[sequence_name] = ""

                elif sequence_name is not None:
                    sequences[sequence_name] += line

    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        return {}

    return sequences


def analyze_sequences(sequences):
    """
    Analyze multiple DNA sequences.

    Args:
        sequences (dict): DNA sequences.

    Returns:
        dict: Analysis results.
    """

    results = {}

    for name, sequence in sequences.items():

        if not validate_sequence(sequence):
            continue

        results[name] = {
            "length": len(sequence),
            "gc_content": calculate_gc_content(sequence),
            "counts": count_bases(sequence),
            "reverse_complement": reverse_complement(sequence)
        }

    return results


def print_report(results, show_reverse_complement=False):
    """
    Print sequence analysis results.

    Args:
        results (dict): Analysis results.
        show_reverse_complement (bool): Whether to display reverse complements.
    """

    for name, data in results.items():

        print("\nSequence:", name)
        print("Length:", data["length"])
        print("GC Content:", data["gc_content"], "%")

        print("A:", data["counts"]["A"])
        print("T:", data["counts"]["T"])
        print("C:", data["counts"]["C"])
        print("G:", data["counts"]["G"])

        if show_reverse_complement:
            print(
                "Reverse Complement:",
                data["reverse_complement"]
            )


def write_csv(results, filename):
    """
    Write analysis results to a CSV file.

    Args:
        results (dict): Analysis results.
        filename (str or Path): Output CSV location.
    """

    filename = Path(filename)

    filename.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Sequence",
            "Length",
            "GC_Content",
            "A",
            "T",
            "C",
            "G",
            "Reverse_Complement"
        ])

        for name, data in results.items():

            writer.writerow([
                name,
                data["length"],
                data["gc_content"],
                data["counts"]["A"],
                data["counts"]["T"],
                data["counts"]["C"],
                data["counts"]["G"],
                data["reverse_complement"]
            ])


def main():

    parser = argparse.ArgumentParser(
        description="Analyze DNA sequences from FASTA files"
    )

    parser.add_argument(
        "filename",
        help="FASTA file containing DNA sequences"
    )

    parser.add_argument(
        "--reverse-complement",
        action="store_true",
        help="Display reverse complement sequences"
    )

    args = parser.parse_args()

    sequences = read_fasta(args.filename)

    if not sequences:
        print("No sequences found.")
        return

    results = analyze_sequences(sequences)

    if not results:
        print("No valid DNA sequences found.")
        return

    print_report(
        results,
        args.reverse_complement
    )

    output_file = "results/results.csv"

    write_csv(results, output_file)

    print(f"\nResults saved to {output_file}")


if __name__ == "__main__":
    main()