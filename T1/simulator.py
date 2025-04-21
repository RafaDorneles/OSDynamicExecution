from reader import Reader
from scheduler import EDFScheduler
from task import Task

class Simulator:

    def _run(self):
        self._simulator()

    def _simulator(self):
        scheduler = EDFScheduler()

        input_files = [
            {"path": "inputFiles/prog1.txt", "arrival_time": 1, "computation_time": 4, "period": 10},
            {"path": "inputFiles/prog2.txt", "arrival_time": 2, "computation_time": 5, "period": 15},
            {"path": "inputFiles/prog3.txt", "arrival_time": 1, "computation_time": 4, "period": 10},
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