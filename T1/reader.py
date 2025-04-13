class Reader:
    
    prefix_map = {
        "ADD": "arithmetic",
        "SUB": "arithmetic",
        "MULT": "arithmetic",
        "DIV": "arithmetic",
        "LOAD": "memory",
        "STORE": "memory",
        "BRANY": "jump",
        "BRZERO": "jump",
        "BRPOS": "jump",
        "BRNEG": "jump",
        "SYSCALL": "system",
    }

    @staticmethod
    def _load_File(path):
        with open(path, 'r') as f:
            lines = f.readlines()

        instructions = []
        data = []
        labels = {}
        current_section = None
        program_counter = 0

        for raw_line in lines:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            match line.lower():
                case ".code":
                    current_section = "code"
                    continue
                case ".endcode":
                    current_section = None
                    continue
                case ".data":
                    current_section = "data"
                    continue
                case ".enddata":
                    current_section = None
                    continue

            if current_section == "code":
                mode = "direct"
                instruction_type = None

                if ":" in line:
                    label, rest = line.split(":", 1)
                    labels[label.strip()] = program_counter 
                    line = rest.strip() 
                    if not line: 
                        continue

                upper_line = line.upper()
                op = upper_line.split()[0]

                instruction_type = Reader.prefix_map.get(op)

                if instruction_type in ["arithmetic", "memory"] and op != "STORE":
                    if "#" in line:
                        mode = "immediate"

                instructions.append({
                    "instruction": line,
                    "mode": mode,
                    "type": Reader.prefix_map.get(op),
                })
                program_counter += 1

            elif current_section == "data":
                data.append(line)

        return instructions, data, labels
