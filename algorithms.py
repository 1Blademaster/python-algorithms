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

def calcTime(func, args):
	startTime = time.perf_counter()
	func(args)
	actualEndTime = time.perf_counter() - startTime
	formatEndTime = '{:.15f}'.format(float(actualEndTime))

	return formatEndTime, actualEndTime

if __name__ == '__main__':
	randomNumList = []
	for i in range(1000):
		randomNumList.append(random.randint(0, 10000))

	bubbleSortTime, actualBubbleSortTime = calcTime(bubbleSort, randomNumList)
	selectionSortTime, actualSelectionSortTime = calcTime(selectionSort, randomNumList)

	percentageDifference = ((actualBubbleSortTime - actualSelectionSortTime) / ((actualBubbleSortTime + actualSelectionSortTime) / 2)) * 100

	print(f'Time for bubble sort: {bubbleSortTime}s')
	print(f'Time for selection sort: {selectionSortTime}s')
	print(f'Percentage difference between algorithms: {percentageDifference}%')
	