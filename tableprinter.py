print("name=pushpa,usn=1AY24AI086,section=O")
def print_table(data):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
    for row in data:
        print("|".join(str(item).ljust(width) for item, width in zip(row, col_widths)))
table_data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

print_table(table_data)