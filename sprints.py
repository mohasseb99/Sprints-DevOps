def MyFunc(numbers):
    evenInt = 0
    cnt = 0
    maxFloat = -99999999
    for num in numbers:
        if num % 2 == 0:
            evenInt += num
            cnt += 1
        elif num % 1 != 0:
            maxFloat = max(maxFloat, num)

    if cnt == 0 and maxFloat == -99999999:
        return 0

    if cnt != 0:
        evenInt = evenInt / cnt

    if maxFloat == -99999999:
        maxFloat = "none"

    return [evenInt, maxFloat]