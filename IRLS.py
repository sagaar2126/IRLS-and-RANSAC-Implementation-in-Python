## IRLS algorithm
from numpy.linalg import inv
import numpy as np
import random
import matplotlib.pyplot as plt

def IRLS(A,y,max_iter,tolerance):
    #vector X is is datapoint x1,x2...xn with 1 column appended with all entires equal to 1...
    A=np.vstack([A, np.ones(len(A))]).T
    X=np.dot(inv(np.dot(np.transpose(A),A)),np.dot(np.transpose(A),y))
    for i in range(max_iter):
        X_=X
        
        e=abs(y-np.dot(A,X))
        f=np.divide(np.power(e,2),(np.power(e,2)+1))
        W=np.diag(f)
        X=np.dot(inv(np.dot(np.transpose(A),np.dot(W,A))),np.dot(np.transpose(A),np.dot(W,y)))
        tol=np.sum(abs(X-X_))
        if(tol<tolerance):
            return X
        
    return X 
   
def setup2():
    inliersTolerance = 2
    inliersCount = 80
    inliers = [(i + random.gauss(0,0.6)*inliersTolerance, 
            2*(i + random.gauss(0,0.6)*inliersTolerance))
            for i in range(0, inliersCount)]

    outliersCount = 20
    outliers = [(random.gauss(0,0.6)*outliersCount, 
              2*(random.gauss(0,0.6)*outliersCount))
            for i in range(0, outliersCount)]


    allpoints = inliers + outliers
      # for point in allpoints:
      #     plt.scatter(point[0], point[1], color="blue")
      # plt.title('Sample Points for Ransac 2D Algorithm')
      # plt.show()

    data=np.array(allpoints)
    X=IRLS(data[:,0],data[:,1],20,0.001)
    plt.scatter(np.array(allpoints)[:,0],np.array(allpoints)[:,1] , c='green') 
    plt.plot(data[:,0], np.dot(X,np.vstack([data[:,0],np.ones(len(data[:,0]))])), color="red")
    plt.title('Line Fitted through points in 2D using IRLS')
    plt.gca()
    plt.show()

def setup1():
    
    count=100
    Tolerance = 25

    datapoints = [(i + random.gauss(0,0.6)*Tolerance, 
            2*(i + random.gauss(0,0.6))*Tolerance)
           for i in range(0, count)]

    allpoints = datapoints
    data=np.array(allpoints)
    X=IRLS(data[:,0],data[:,1],20,0.001)
    plt.scatter(np.array(allpoints)[:,0],np.array(allpoints)[:,1] , c='green') 
    plt.plot(data[:,0], np.dot(X,np.vstack([data[:,0],np.ones(len(data[:,0]))])), color="red")
    plt.title('Line Fitted through points in 2D using IRLS')
    plt.gca()
    plt.show()

def main():
    setup1()
    setup2()
if __name__ == "__main__":
    main()
    