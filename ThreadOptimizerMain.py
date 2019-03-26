## TO-ADD: Periodically check runtime of function while running and if it exceeds previous shortest runtime short-circuit

import random
import threading
import os
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
from queue import Queue
from collections import deque

def main():
	## The main function
	deq = deque(readUrlTestFile("randomUrls.txt"))
	soupList = []

	rt = estimateExpectedRunTime(workQ, 8, 10, testFunction, [soupList])
	
	print(rt)

def estimateExpectedRunTime(workQ, sampleSize, threadCount, iterations, foo, fooArgs):
	deq = deque()
	
	for i in range(workQ.qsize()):
		item = workQ.get()
		deq.append(item)
		workQ.put(item)

	runTimes = []
	
	for i in range(iterations):
		sample = getRandomSample(deq, sampleSize)
		print(i)
		runTimes.append(runTest(sample, threadCount, foo, fooArgs))

	return sum(runTimes) / float(iterations)

## Test function that takes a url string, opens it, and puts the request object into a BeautifulSoup object
def testFunction(soupList, urlQ):
	while not urlQ.empty():

		if urlQ.qsize() % 10 == 0:
			print("\tApproximately {} items remaining.".format(urlQ.qsize()))

		url = urlQ.get()

		if url == None:
			break

		try:
			page = urlopen(url)
			soupList.append(BeautifulSoup(page, "html.parser").encode("utf-8"))
		
		except Exception:
			pass

		urlQ.task_done()


def runTest(sample, threadCount, foo, fooArgs):
	startTime = time.time()
	sampleQ = Queue()

	argsCopy = fooArgs.copy()

	for item in sample:
		sampleQ.put(item)

	argsCopy.append(sampleQ)
	print("fooArgs Length: {}".format(len(fooArgs)))
	threads = []

	for i in range(threadCount):
		t = threading.Thread(target=foo, args=tuple(argsCopy))
		t.start()
		threads.append(t)

	sampleQ.join()

	for i in range(threadCount):
		sampleQ.put(None)

	for t in threads:
		t.join()

	return time.time() - startTime

## Opens url test file, parses the urls into a list, closes the url test file, and returns the list
def readUrlTestFile(urlFileName):
	urlFile = open(urlFileName, "r")

	urls = urlFile.read().split("\n")

	urlFile.close()

	return urls

def getRandomSample(deq, size):
	if type(deq).__name__ != "deque":
		raise Exception("Invalid Input: deq must be of type 'deque'")

	if type(size).__name__ != "int":
		raise Exception("Invalid Input: size must be of type 'int'")

	if size <= 0:
		raise Exception("Invalid Input: size must be a positive, non-zero integer")

	if size > len(deq):
		raise Exception("Invalid Input: size must be less than or equal to the length of the the queue")
	
	return random.sample(deq, size)

main()