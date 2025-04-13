class Program:

    def loadFile(path):
        with open(path, 'r') as f:
            lines = f.readlines()

        code_lines = []
        data_lines = []
        current_section = None

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  

            if line == ".code":
                current_section = "code"
                continue
            elif line == ".endcode":
                current_section = None
                continue
            elif line == ".data":
                current_section = "data"
                continue
            elif line == ".enddata":
                current_section = None
                continue

            if current_section == "code":
                code_lines.append(line)
            elif current_section == "data":
                data_lines.append(line)

        return code_lines, data_lines