from tabulate import tabulate

rooms_list = {'lounge': {'tv': 200,
                         'couch': 500,
                         'side table': 150,
                         'heater': 195,
                         'bin': 50},
              'bedroom': {'bed': 1000,
                          'lamp': 75,
                          'clothes-dryer': 30,
                          'basket': 50,
                          'dresser': 400}
              }

rooms_tuple = ((k, item, cost) for k, v in rooms_list.items()
               for item, cost in v.items())
room_table = tabulate(rooms_tuple, headers=['room', 'item', 'value'])
print(room_table)

rooms_costs = {}
for room in rooms_list:
    room_cost = sum(cost for item, cost in rooms_list[room].items())
    rooms_costs[room] = room_cost,

print(tabulate(rooms_costs, headers='keys'))
