from program import Program

code, data = Program.loadFile("./inputFiles/prog1.txt")
code, data = Program.loadFile("./inputFiles/prog2.txt")


print("Code Section:")
print("\n".join(code))
print("\nData Section:")
print("\n".join(data))