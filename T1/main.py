from reader import Reader
from process import Process

def main():
    instructions, data, labels = Reader._load_File("./inputFiles/prog1.txt")
    print("Labels carregados:", labels)
    program = Process(instructions, data, labels)
    program.execute()

if __name__ == "__main__":
    main()