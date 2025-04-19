import random
import time
from enum import Enum

class State(Enum):
    READY = "READY"
    BLOCKED = "BLOCKED"
    RUNNING = "RUNNING"
    TERMINATED = "TERMINATED"

class Process:
    pid = 0  

    def __init__(self, instructions, data, labels):
        self.instructions = instructions         
        self.labels = labels                  
        self.data = self._parse_data(data)
        self.pc = 0  
        self.acc = 0 
        self.state = State.READY
        self.block_duration = 0
        Process.pid += 1
        self.pid = Process.pid
        self.input_locked = set()
        
    def _parse_data(self, data):
        parsed_data = {}
        for line in data:
            parts = line.split()
            if len(parts) == 2:
                label, value = parts
                parsed_data[label] = int(value)
        return parsed_data

    def execute(self):
        self.state = State.RUNNING
        print(f"Process {self.pid}.")

        while self.state != State.TERMINATED and self.pc < len(self.instructions):
            instr = self.instructions[self.pc]
            parts = instr["instruction"].split()
            op = parts[0].upper()
            operand = parts[1] if len(parts) > 1 else None  

            if op == "LOAD":
                self._load(operand)
            elif op == "DIV":
                self._div(operand)
            elif op == "MULT":
                self._mult(operand)
            elif op == "ADD":
                self._add(operand)
            elif op == "STORE":
                self._store(operand)
            elif op == "SUB":
                self._sub(operand)
            elif op == "SYSCALL":
                self._syscall(int(operand))
            elif op in ["BRANY", "BRZERO", "BRPOS", "BRNEG"]:
                self._jump(op, operand)
                continue  
            else:
                raise ValueError(f"Unknown instruction: {op}")

            self.pc += 1  

        print("\nFinal data:")
        for key, value in self.data.items():
            print(f"{key}: {value}")

    def _sub(self, operand):
        if operand.startswith("#"):  
            self.acc -= int(operand[1:])
        else:  
            self.acc -= self.data.get(operand, 0)

    def _div(self, operand):
        if operand.startswith("#"):  
            divisor = int(operand[1:])
        else:  
            divisor = self.data.get(operand, 0)

        if divisor == 0:
            raise ZeroDivisionError("Division by zero.")
        else:
            self.acc //= divisor

    def _mult(self, operand):
        if operand.startswith("#"):  
            self.acc *= int(operand[1:])
        else:  
            self.acc *= self.data.get(operand, 0)

    def _jump(self, op, operand):
        accumulator = self.acc - 1

        if op == "BRANY":
            self.pc = self.labels[operand]
        elif op == "BRZERO" and accumulator == 0:
            self.pc = self.labels[operand]
        elif op == "BRPOS" and accumulator > 0:
            self.pc = self.labels[operand]
        elif op == "BRNEG" and accumulator < 0:
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
            value = self.data.get(operand, 0)
            self.acc += value

    def _store(self, operand, value=None):
        if operand in self.data: 
            self.data[operand] = value if value is not None else self.acc

    def _syscallInput(self, target_variable):
            try:
                user_input = int(input(f"Type a number for {target_variable}: "))
                self.data[target_variable] = user_input
                self.acc = user_input 
                self.input_locked.add(target_variable)
            except ValueError:
                print("Invalid input.")
            self.state = State.READY 

    def _syscall(self, code):
        if code == 0: 
            self.state = State.TERMINATED
        elif code == 1:  
            print(f"ACC: {self.acc}")
        elif code == 2:  
            target_variable = self.instructions[self.pc - 1]["instruction"].split()[1]  
            self._syscallInput(target_variable)
        else:
            raise ValueError(f"Unknown syscall code: {code}")


