import json
import sys


def move(command):
    record = {'moves': [command]}
    print(json.dumps(record))
    sys.stdout.flush()


def afstand(planeet1, planeet2):
    return ((planeet1['x'] - planeet2['x']) ** 2 + (planeet1['y'] - planeet2['y']) ** 2)**(1/2)


for line in sys.stdin:
    state = json.loads(line)

    my_planets = [p for p in state['planets'] if p['owner'] == 1]
    other_planets = [p for p in state['planets'] if p['owner'] != 1]
    empty_planets = [p for p in other_planets if p['owner'] is None or p['owner'] == 0]
    mytotalShips = sum()

    totalShips = sum(p['ship_count'] for p in state['planets'])

    if not my_planets:
        move(None)
        continue

    if empty_planets:
        myplanet = max(my_planets, key=lambda p: p['ship_count'])
        otherplanet = min(empty_planets, key=lambda p: afstand(myplanet, p))
        shipAmount = 7
        if myplanet['ship_count'] < shipAmount:
            move(None)
        else:
            move({
                'origin': myplanet['name'],
                'destination': otherplanet['name'],
                'ship_count': shipAmount
            })
    elif other_planets:
        myplanet = max(my_planets, key=lambda p: p['ship_count'])
        otherplanet = min(other_planets, key=lambda p: afstand(myplanet, p))

        shipAmount = otherplanet['ship_count'] + 3
        if myplanet['ship_count'] < shipAmount:
            move(None)
        else:
            move({
                'origin': myplanet['name'],
                'destination': otherplanet['name'],
                'ship_count': shipAmount
            })
    else:
        move(None)
