
def load_values(file):
    values = []
    variables = 0
    clauses = 0
    max_var = 0
    with open(file, "r") as ins:
        array = []
        for line in ins:
            if len(line) < 2:
                continue
            if line[0] == 'c':
                continue
            if line[0] == 'p':
                problem_line = line.split(" ")
                variables = int(problem_line[2])
                clauses = int(problem_line[3])
                continue

            splitted = line.split(" ")
            end_of_line = splitted[len(splitted) - 1]
            if end_of_line[0] == '0':
                line_val = []
                for num_str in splitted:
                    num = int(num_str)
                    if num > 0 or num < 0:
                        ins_val = (1 if num > 0 else 0, abs(num)-1)
                        max_var = max(max_var, ins_val[1])
                        line_val.append(ins_val)
                values.append(line_val)
    return values, variables, clauses