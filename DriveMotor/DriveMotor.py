def fill_row() -> list:
    row = []
    row.extend(['-'] + ['.' for j in range(18)] + ['-'])
    return row

def initialize() -> list:
    field = []
    for i in range(20):
        row = []
        if i == 0 or i == 19:
            row.extend(['-' for j in range(20)])
        else:
            row.extend(fill_row())
        field.append(row)
    return field

def print_test(field):
    for i in range(20):
        row = ''
        for j in range(20):
            row += field[i][j]
        print(row)

print_test(initialize())