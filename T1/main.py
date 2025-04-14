from reader import Reader
from program import Program

def main():
    instructions, data, labels = Reader._load_File("./inputFiles/prog2.txt")
    print("Labels carregados:", labels)
    program = Program(instructions, data, labels)
    program.execute()

if __name__ == "__main__":
    main()