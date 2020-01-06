#https://stackabuse.com/sorting-algorithms-in-python/

import time
import random

def bubbleSort(num_list):
	for i in range(len(num_list)):
		for j in range(len(num_list) - 1):
			if num_list[j] > num_list[j + 1]:
				num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

	return num_list

def selectionSort(num_list):
	for i in range(len(num_list)):
		lowestValueIndex = i
		for j in range(i + 1, len(num_list)):
			if num_list[j] < num_list[lowestValueIndex]:
				lowestValueIndex = j
		num_list[i], num_list[lowestValueIndex] = num_list[lowestValueIndex], num_list[i]

	return num_list

def insertionSort(num_list):
	for i in range(1, len(num_list)):
		j = i - 1
		while j >= 0 and num_list[j] > num_list[i]:
			num_list[i] = num_list[j]
			j -= 1
		num_list[j + 1] = num_list[i]

	return num_list

def quickSortPartition(num_list, low, high):
	pivotPoint = num_list[(low + high) // 2]
	i = low - 1
	j = high + 1
	while True:
		i += 1
		while num_list[i] < pivotPoint:
			i += 1

		j -= 1
		while num_list[j] > pivotPoint:
			j -= 1

		if i >= j:
			return j

		num_list[i], num_list[j] = num_list[j], num_list[i]

def quickSort(num_list):
	def _quickSort(items_list, low, high):
		if low < high:
			splitIndex = quickSortPartition(items_list, low, high)
			_quickSort(items_list, low, splitIndex)
			_quickSort(items_list, splitIndex + 1, high)
	
	_quickSort(num_list, 0, len(num_list) - 1)

	return num_list

def calcTime(func, args):
	startTime = time.perf_counter()
	func(args)
	actualEndTime = time.perf_counter() - startTime
	formatEndTime = '{:.15f}'.format(float(actualEndTime))

	return formatEndTime, actualEndTime

if __name__ == '__main__':
	randomNumList = [random.randint(0, 10000) for iter in range(100000)]

	bubbleSortTime, actualBubbleSortTime = calcTime(bubbleSort, randomNumList)
	selectionSortTime, actualSelectionSortTime = calcTime(selectionSort, randomNumList)
	insertionSortTime, actualInsertionSortTime = calcTime(insertionSort, randomNumList)
	quickSortTime, actualQuickSortTime = calcTime(quickSort, randomNumList)

	print(f'Time for bubble sort: {bubbleSortTime}s')
	print(f'Time for selection sort: {selectionSortTime}s')
	print(f'Time for insertion sort: {insertionSortTime}s')
	print(f'Time for quick sort: {quickSortTime}s')
	