start_symbol = 'S'
productions = {
    'S': [['NP', 'VP']],
    'NP': [['John'], ['Mary']],
    'VP': [['eats'], ['sleeps']]
}
input_str = "Mary sleeps"
tokens = input_str.split()
chart = {}
for production in productions[start_symbol]:
    chart[start_symbol] = [(0, production)]
for i in range(len(tokens) + 1):
    for symbol in list(chart):
        for entry in chart[symbol]:
            if len(entry[1]) > i:
                next_symbol = entry[1][i]
                if next_symbol in productions:
                    for production in productions[next_symbol]:
                        chart[next_symbol] = chart.get(next_symbol, []) + [(i, production)]
if (len(tokens), [start_symbol]) in chart.get(start_symbol, []):
    print("Input string parsed successfully")
else:
    print("Invalid input string")
