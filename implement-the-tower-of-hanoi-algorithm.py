def hanoi_solver(disks):
    rods = {
        'A': list(range(disks, 0, -1)),
        'B': [],
        'C': []
    }

    moves = []
    moves.append(f"{rods['A']} {rods['B']} {rods['C']}")

    def move(n, start, target, aux):
        if n == 1:
            disk = rods[start].pop()
            rods[target].append(disk)
            moves.append(f"{rods['A']} {rods['B']} {rods['C']}")
        else:
            move(n-1, start, aux, target)
            disk = rods[start].pop()
            rods[target].append(disk)
            moves.append(f"{rods['A']} {rods['B']} {rods['C']}")

            move(n-1, aux, target, start)

    move(disks, 'A', 'C', 'B')

    return '\n'.join(moves)

print(hanoi_solver(3))
print(hanoi_solver(4))
