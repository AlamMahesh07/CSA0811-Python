arr = [1, 3, 2, 4, 6, 5]
peaks = []
if len(arr) == 1 or arr[0] >= arr[1]:
    peaks.append(arr[0])
if arr[-1]>= arr[-2]:
    peaks.append(arr[-1])
for i in range(1, len(arr) - 1):
    if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
        peaks.append(arr[i])
if peaks:
    print("Peak elements:", peaks)
else:
    print("No peak elements found")
