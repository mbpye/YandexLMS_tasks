petia_speed = int(input())
vasia_speed = int(input())
tolya_speed = int(input())

speeds = {'Петя': petia_speed, 'Вася': vasia_speed, 'Толя': tolya_speed}

sorted_speeds = sorted(speeds.items(), key=lambda x: x[1], reverse=True)

print(f'          {sorted_speeds[0][0]}\n  {sorted_speeds[1][0]}')
print(f'                  {sorted_speeds[2][0]}\n   II      I      III   ')




