from reader import Reader
from scheduler import EDFScheduler
from task import Task

class Simulator:

    def _run(self):
        self._simulator()

    def _simulator(self):
        scheduler = EDFScheduler()

        input_files = [
            {"path": "inputFiles/prog3.txt", "arrival_time": 0, "computation_time": 77, "period": 100},
            {"path": "inputFiles/prog2.txt", "arrival_time": 0, "computation_time": 78, "period": 120},
            {"path": "inputFiles/prog1.txt", "arrival_time": 0, "computation_time": 80, "period": 150},
            {"path": "inputFiles/prog4.txt", "arrival_time": 0, "computation_time": 80, "period": 200},
            {"path": "inputFiles/prog5.txt", "arrival_time": 0, "computation_time": 80, "period": 250},
        ]

        for file in input_files:
            instructions, data, labels = Reader._load_File(file["path"])

            task = Task(instructions, data, labels, file["path"])

            scheduler._add_process(
                task=task,
                arrival_time=file["arrival_time"],
                computation_time=file["computation_time"],
                period=file["period"]
            )

        scheduler._show_processes()
        scheduler._run()