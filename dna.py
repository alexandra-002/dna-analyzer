
sequence = input("Enter a DNA sequence: ").upper()

valid_bases = "ATCG"
is_valid = True

for base in sequence:
	if base not in valid_bases:
		is_valid = False

if not is_valid:
	print("Invalid DNA sequence")
else:
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
