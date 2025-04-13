class Program:
    def __init__(self, instructions, data, labels):
        self.instructions = instructions         
        self.labels = labels                     
        self.data = self._parse_data(data)
        self.pc = 0
        self.acc = 0
        self.halted = False
        self.blocked = False
        self.block_duration = 0

    def _parse_data(self, data):
        parsed_data = {}
        for line in data:
            parts = line.split()
            if len(parts) == 2:
                label, value = parts
                parsed_data[label] = int(value)
            elif len(parts) == 1:
                label = parts[0]
                parsed_data[label] = None
        return parsed_data
    
    def run(self):
        while not self.halted and not self.blocked:
            instruction = self.instructions[self.pc]
            self.execute(instruction)
            if not self.blocked:
                self.pc += 1
        if self.halted:
            print("Program halted.")    
        elif self.blocked:
            print(f"Program blocked for {self.block_duration} cycles.")

    
    

