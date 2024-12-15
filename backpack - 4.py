bag = []
curr_count = 3 * 3
points = 15

items = {'r': [3, 25],
         'p': [2, 15],
         'a': [2, 15],
         'm': [2, 20],
         'i': [1, 5],
         'k': [1, 15],
         'x': [3, 20],
         't': [1, 25],
         'f': [1, 15],
         'd': [1, 10],
         's': [2, 20],
         'c': [2, 20]
}
d_weight, d_points = items['d']

for key in items:
    weight, survival_points = items[key]
    efficiency = survival_points / weight
    items[key].append(efficiency)


items = sorted(items.items(), key=lambda x: x[1][2], reverse=True)


bag.append('d')
curr_count -= d_weight
points += d_points

for key, (weight, survival_points, efficiency) in items:
    if key != 'd' and curr_count >= weight:
        bag.extend([key] * weight)
        curr_count -= weight
        points += survival_points
    elif key != 'd':
        points -= survival_points


inventory = [[" " for _ in range(3)] for _ in range(3)]
for i, item in enumerate(bag):
    row, col = divmod(i, 3)
    inventory[row][col] = f"[{item}]"


for row in inventory:
    print(", ".join(row))
print('\n', 'Итоговые очки выживания:', points)
