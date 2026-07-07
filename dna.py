
sequence = input("Enter a DNA sequence: ").upper()

length = len(sequence)

g_count = sequence.count("G")
c_count = sequence.count("C")

gc_content = ((g_count + c_count) / length) * 100

print("Sequence:", sequence)
print("Length:", length)
print ("GC Content:", round(gc_content, 2), "%")