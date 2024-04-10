def draw_table():
    result = ''
    for i in range(1, 11):
        row = ''
        for j in range(1, 11):
            row += f"{i * j:4}"
        result += row + '\n'
    return result

print(draw_table())