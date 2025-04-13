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
        return parsed_data

    def execute(self):
        while not self.halted and self.pc < len(self.instructions):
            instr = self.instructions[self.pc]
            parts = instr["instruction"].split()
            op = parts[0].upper()
            operand = parts[1] if len(parts) > 1 else None  

            if op == "LOAD":
                self._load(operand)
            elif op == "ADD":
                self._add(operand)
            elif op == "STORE":
                self._store(operand)
            elif op == "SYSCALL":
                self._syscall(int(operand))
            elif op in ["BRANY", "BRZERO", "BRPOS", "BRNEG"]:
                self._jump(op, operand)
            else:
                raise ValueError(f"Operação desconhecida: {op}")

            self.pc += 1  

    def _jump(self, op, operand):
        value = self.acc

        if op == "BRANY":
            self.pc = self.labels[operand]
        elif op == "BRZERO" and value == 0:
            self.pc = self.labels[operand]
        elif op == "BRPOS" and value > 0:
            self.pc = self.labels[operand]
        elif op == "BRNEG" and value < 0:
            self.pc = self.labels[operand]
        else:
            self.pc += 1

    def _load(self, operand):
        if operand.startswith("#"): 
            self.acc = int(operand[1:])
        else:  
            self.acc = self.data.get(operand, 0)

    def _add(self, operand):
        if operand.startswith("#"):  
            self.acc += int(operand[1:])
        else:  
            self.acc += self.data.get(operand, 0)

    def _store(self, operand):
        if operand in self.data: 
            self.data[operand] = self.acc
        else:
            raise ValueError(f"Variável desconhecida: {operand}")

    def _syscall(self, code):
        if code == 0: 
            self.halted = True
        elif code == 1:  
            print(f"ACC: {self.acc}")
        elif code == 2:  
            print("Data Section:")
            for key, value in self.data.items():
                print(f"{key}: {value}")
        else:
            raise ValueError(f"Código de syscall desconhecido: {code}")