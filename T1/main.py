from program import Program

code, data = Program.loadFile("T1/inputFiles/prog1.txt")
code, data = Program.loadFile("T1/inputFiles/prog2.txt")

print("Code Section:")
print("\n".join(code))
print("\nData Section:")
print("\n".join(data))