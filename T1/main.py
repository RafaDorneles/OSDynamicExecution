from reader import Reader

instructions, data, labels = Reader._load_File("T1/inputFiles/prog1.txt")

print("\nCode Section:")
print("\n".join([f"{instr['instruction']} ({instr['mode']})" for instr in instructions]))
print("\nData Section:")
print("\n".join(data))
print("\nLabels:")
print("\n".join([f"{label}: {position}" for label, position in labels.items()]))
print("=============================================")

instructions, data, labels = Reader._load_File("T1/inputFiles/prog2.txt")

print("\nCode Section:")
print("\n".join([f"{instr['instruction']} ({instr['mode']})" for instr in instructions]))
print("\nData Section:")
print("\n".join(data))
print("\nLabels:")
print("\n".join([f"{label}: {position}" for label, position in labels.items()]))