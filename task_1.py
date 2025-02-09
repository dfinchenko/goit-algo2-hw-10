import random
import time
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_function, arr, runs=5):
    total_time = 0
    for _ in range(runs):
        arr_copy = arr[:]
        start_time = time.time()
        sort_function(arr_copy)
        total_time += time.time() - start_time
    return total_time / runs

sizes = [10_000, 50_000, 100_000, 500_000]
rand_quick_times = []
det_quick_times = [] 

for size in sizes:
    arr = [random.randint(0, 1_000_000) for _ in range(size)]
    rand_quick_time = measure_time(randomized_quick_sort, arr)
    det_quick_time = measure_time(deterministic_quick_sort, arr)
    
    rand_quick_times.append(rand_quick_time)
    det_quick_times.append(det_quick_time)

    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_quick_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_quick_time:.4f} секунд")

print("\nВисновок:")
print("Результати тестування підтверджують, що хоча теоретично рандомізований QuickSort має певну перевагу в порівнянні з детермінованим, реальні результати часто залежать від системних оптимізацій. "
      "Для менших масивів різниця в часі виконання між рандомізованим і детермінованим алгоритмами незначна, при цьому іноді детермінований алгоритм може працювати швидше. "
      "Для великих масивів час виконання обох алгоритмів практично однаковий, що вказує на те, що системні оптимізації, такі як кешування або ефективна обробка даних, можуть знижувати перевагу рандомізованого підходу.")

plt.figure(figsize=(10, 6))
plt.title('Порівняння рандомізованого та детермінованого QuickSort')
plt.plot(sizes, rand_quick_times, marker='o', label='Рандомізований QuickSort')
plt.plot(sizes, det_quick_times, marker='s', label='Детермінований QuickSort')
plt.xlabel('Розмір масиву')
plt.ylabel('Середній час виконання (секунди)')
plt.legend()
plt.grid()
plt.show()
