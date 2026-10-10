# loop_breaker
for i in range(1, 21):
    if i == 18:
        break
    if i == 13:
        continue
    if i % 4 == 0:
        pass 
    print(i)