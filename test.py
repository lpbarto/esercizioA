from classes import RN, ABR
import numpy as np
from timeit import default_timer as timer
import sys
import csv
import matplotlib.pyplot as plt
sys.setrecursionlimit(100000)

def random_list(n):
    # Permutazione casuale dei primi n interi
    A = np.arange(n)
    np.random.shuffle(A)
    return A

def mediat(tempi):
    avarage = np.mean(tempi)
    avarage = float(avarage)
    return round(avarage, 5)

def testMAx(tree):
    startTime = timer()
    tree.findMax(tree.root)
    endTime = timer()
    return endTime - startTime


def testInsert(nstart, nmax, gap):
    startTestTime = timer()
    row = ['n', 'ABRr', 'RNr', 'ABRo', 'RNo', 'tmaxABRr', 'tmaxRNr', 'tmaxABRo', 'tmaxRNo']
    with open('testInsert.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()

    times = np.arange(10, dtype='f')
    timesmax = np.arange(10, dtype='f')


    for n in range(nstart, nmax, gap):

        for y in range(0, 10, 1):
            # Inserimento Random ABR
            treeA = ABR()
            startInsertRandom = timer()
            A = random_list(n)
            for x in A:
                 treeA.insert(x)
            endInsertRandom = timer()
            times[y] = endInsertRandom - startInsertRandom
            #test max
            timesmax[y] = testMAx(treeA)
        tABRr = mediat(times)
        tmaxABRr = np.mean(timesmax)

        for y in range(0, 10, 1):
            # Inserimento Random RN
            treeRNb = RN()
            startInsertRnRandom = timer()
            A = random_list(n)
            for x in A:
                treeRNb.insert(x)
            endInsertRnRandom = timer()
            times[y] = endInsertRnRandom - startInsertRnRandom
            # test max
            timesmax[y] = testMAx(treeRNb)
        tRNr = mediat(times)
        tmaxRNr = np.mean(timesmax)

        for y in range(0, 10, 1):
            #inserimento ordinato ABR
            tree = ABR()
            startInsert = timer()
            for x in range(0, n//10):
                tree.insert(x)
            endInsert = timer()
            times[y] = endInsert - startInsert
            # test max
            timesmax[y] = testMAx(tree)
        tABRo = mediat(times)
        tmaxABRo = np.mean(timesmax)

        for y in range(0, 10, 1):
            # Inserimento ordinato RN
            treeRNa = RN()
            startInsertRnOrdinato = timer()
            for x in range(0, n):
                treeRNa.insert(x)
            endInsertRnOrdinato = timer()
            times[y] = endInsertRnOrdinato - startInsertRnOrdinato
            # test max
            timesmax[y] = testMAx(treeRNa)
        tRNo = mediat(times)
        tmaxRNo = np.mean(timesmax)

        dataCsv = [n, tABRr, tRNr, tABRo, tRNo, tmaxABRr, tmaxRNr, tmaxABRo, tmaxRNo]
        with open('testInsert.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(dataCsv)
        csvFile.close()

    data = np.loadtxt('testInsert.csv', delimiter=",", skiprows=1,usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8])

    plt.figure(1)
    plt.subplot(211)
    plt.plot(data[:, 0], data[:, 1], label='ABRr')
    plt.plot(data[:, 0], data[:, 2], label='RNr')
    plt.plot(data[:, 0], data[:, 4], label='RNo')
    # plt.plot(data[:, 0]//10, data[:, 3], label='ABRo')
    plt.xlabel('n')
    plt.ylabel('time(s)')
    plt.title("inserimento")
    plt.legend()

    plt.subplot(212)
    plt.plot(data[:, 0], data[:, 5], label='maxABRr')
    plt.plot(data[:, 0], data[:, 6], label='maxRNr')
    plt.plot(data[:, 0], data[:, 8], label='maxRNo')
    # plt.plot(data[:, 0]//10, data[:, 7], label='maxABRo')
    plt.xlabel('n')
    plt.ylabel('time(s)')
    plt.title("search max")
    plt.legend()

    plt.show()





