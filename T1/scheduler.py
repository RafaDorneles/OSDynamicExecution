from task import State
import random

class EDFScheduler:
    def __init__(self):
        self.processes = []  
        self.time = 0  
        self.readyQueue = []  
        self.blockedQueue = []  

    def _add_process(self, task, arrival_time, computation_time, period):
        process = {
            "task": task,
            "arrival_time": arrival_time,
            "computation_time": computation_time,
            "period": period,
            "deadline": arrival_time + period,
            "remaining_time": computation_time,
            "state": State.READY,
        }
        self.processes.append(process)

    def _show_processes(self):
        print("Lista de Processos:")
        for process in self.processes:
            print(f"Processo {process['task'].pid}: " + 
                f"Chegada={process['arrival_time']}, " +
                f"Comp. Time={process['computation_time']}, " +
                f"Período={process['period']}, " +
                f"Deadline={process['deadline']}, " +
                f"Tempo Restante={process['remaining_time']}, " +
                f"Estado={process['state'].value}")

    def _check_deadlines(self):
        for process in self.processes:
            if (process["state"] != State.TERMINATED and 
                self.time > process["deadline"] and 
                process["remaining_time"] > 0):
                print(f"Processo {process['task'].pid} perdeu o deadline! Faltou: {process['computation_time'] - process['remaining_time']}u")
                process["state"] = State.TERMINATED
                print(f"Processo {process['task'].pid} foi terminado devido à perda de deadline.")
                
                if process in self.readyQueue:
                    self.readyQueue.remove(process)
                if process in self.blockedQueue:
                    self.blockedQueue.remove(process)

    def _run(self):
        print("Iniciando o escalonamento EDF...")
        simulation_time = 500  
        
        while self.time < simulation_time and any(p["state"] != State.TERMINATED for p in self.processes):              
            print(f"\n--- Tempo: {self.time} ---")
            
            self._check_deadlines()
            
            for process in self.processes:
                if process["arrival_time"] <= self.time and process["state"] == State.READY and process not in self.readyQueue:
                    self.readyQueue.append(process)
                    print(f"Processo {process['task'].pid} chegou e foi adicionado à fila de prontos")

            for process in self.processes:
                if self.time > 0 and self.time % process["period"] == 0:
                    if process["state"] == State.TERMINATED:
                        print(f"Processo {process['task'].pid} chegou novamente e foi reiniciado.")
                        process["remaining_time"] = process["computation_time"]
                        process["deadline"] = self.time + process["period"]
                        process["state"] = State.READY
                        process["task"].pc = 0
                        process["task"].data = process["task"].initial_data

                        if "block_duration" in process:
                            process["block_duration"] = 0

                        if process not in self.readyQueue:
                            self.readyQueue.append(process)

                        if process not in self.readyQueue:
                            self.readyQueue.append(process)

            self.readyQueue.sort(key=lambda p: p["deadline"])
            
            if self.readyQueue:
                current_process = self.readyQueue.pop(0)
                task = current_process["task"]
                
                current_process["state"] = State.RUNNING
                
                print(f"Executando tarefa {task.pid} (deadline: {current_process['deadline']})")
                
                if task.pc < len(task.instructions):
                    current_instruction = task.instructions[task.pc]
                    instruction_str = current_instruction["instruction"]

                    print(f"  Executando instrução: {instruction_str}")

                    result = task.execute(instruction_str)

                    if result["should_block"]:
                        print(f"  Tarefa {task.pid} bloqueada")
                        current_process["block_duration"] = random.randint(1, 3)
                        current_process["state"] = State.BLOCKED
                        self.blockedQueue.append(current_process)
                    elif result["should_terminate"] or result["completed"]:
                        print(f"  Tarefa {task.pid} terminada")
                        current_process["state"] = State.TERMINATED
                        current_process["remaining_time"] = 0
                        current_process["can_restart"] = True
                    else:
                        current_process["state"] = State.READY
                        self.readyQueue.append(current_process)

                    if current_process["state"] != State.TERMINATED:
                        current_process["remaining_time"] -= 1
                else:
                    print(f"  Tarefa {task.pid} concluiu todas as instruções")
                    current_process["state"] = State.TERMINATED
            else:
                print("Nenhum processo na fila de prontos")
            
            for process in self.blockedQueue[:]:
                process["block_duration"] -= 1
                print(f"Processo {process['task'].pid} bloqueado por mais {process['block_duration']} unidades de tempo")
                
                if process["block_duration"] <= 0:
                    self.blockedQueue.remove(process)
                    if process["state"] != State.READY:
                        process["state"] = State.READY
                        print(f"Estado do processo {process['task'].pid} corrigido para READY.")
                    if process not in self.readyQueue:
                        self.readyQueue.append(process)
                        print(f"Processo {process['task'].pid} desbloqueado e movido para a fila de prontos")
                        
            self.time += 1

        
        print("\nEscalonamento concluído!")