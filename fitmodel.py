import numpy as np
import matplotlib.pyplot as plt
import math


def LeastSquarePolyFit(xData,yData,min_size, order):
    data_number = len(xData)
    coeff = np.array([0] * order)
    if order > data_number or min_size > data_number:
        return 0
    A = np.zeros((data_number, order))
    Y = np.array([0.0] * data_number)
    for i in range(data_number):
        Y[i] = yData[i]
        for j in range(order):
            A[i,j] = math.pow(xData[i],j)
    AT = np.transpose(A)
    ATA = np.matmul(AT,A)
    coeff = np.dot(np.linalg.inv(ATA), np.dot(AT,Y))
    return coeff


def LeastSquareMixPolyFit(xData, yData, min_size, order, freq):
    data_number = len(xData)
    coeff = np.array([0] * order)
    if order > data_number or min_size > data_number:
        return 0
    A = np.zeros((data_number, order))
    Y = np.array([0.0] * data_number)
    for i in range(data_number):
        Y[i] = yData[i]
        A[i,0] = 1
        A[i,1] = xData[i]
        A[i,2] = np.cos(xData[i] * freq)
        A[i,3] = np.sin(xData[i] * freq)

    AT = np.transpose(A)
    ATA = np.matmul(AT, A)
    coeff = np.dot(np.linalg.inv(ATA), np.dot(AT,Y))
    return coeff


def PredMixPolyFit(x1, coeff, freq):
    y_pred = coeff[0] + coeff[1] * x1 + coeff[2] * np.cos(x1 * freq) + coeff[3] * np.sin(x1 * freq)
    return y_pred



def errorCalculate(y,y1):
    e = 0
    if len(y) != len(y1):
        print(" length not equal!")
    dataNumber = len(y)
    if dataNumber <= 0:
        return -1
    for i in range(dataNumber):
        e += (y1[i] - y[i]) * (y1[i] - y[i])
    return e/dataNumber


