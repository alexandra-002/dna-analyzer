
sequence = input("Enter a DNA sequence: ").upper()

length = len(sequence)

g_count = sequence.count("G")
c_count = sequence.count("C")
a_count = sequence.count("A")
t_count = sequence.count("T")

gc_content = ((g_count + c_count) / length) * 100

print("Sequence:", sequence)
print("Length:", length)
print("GC Content:", round(gc_content, 2), "%")
print("A:", a_count)
print("T:", t_count)
print("C:", c_count)
print("G:", g_count)