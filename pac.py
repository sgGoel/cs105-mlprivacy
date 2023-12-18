#DISCLAIMER: ChatGPT was used in this project. The two use cases were: 1) How do I compute X value in Python? or 2) How do I perform X operation in numpy?

import numpy as np

np.random.seed(123)

def noise_determination(M, distrib, m, c, v, beta, r):
    #Lines 2-5: sample m points from the given distribution
    y_labels = np.zeros(m)
    for k in range(m):
        X_k = distrib()
        y_labels[k] = M(X_k)
    
    #Line 6: compute empirical mean and covariance over the sample
    mu_hat = np.mean(y_labels)
    Sigma_hat = np.cov(y_labels, rowvar=False)

    #Line 7: perform signular value decomposition
    U_hat, Lambda_hat, _ = np.linalg.svd(Sigma_hat)
    d = len(Lambda_hat)

    #line 8: Calculate maximal index (ie index of largest eigenvalue)
    j0 = np.argmax(Lambda_hat > c) #am concerned about this line of code; came from chatgpt
    print("Debug: j0", j0)

    #Lines 9-16: Compute Gaussian noise covariance, in two cases. ngl do not understand the math here.
    if np.min([np.abs(Lambda_hat[i] - Lambda_hat[j]) for i in range(j0+1) for j in range(d)]) > r * np.sqrt(d*c) + 2*c:
        Lambda_B = np.zeros_like(Lambda_hat)
        for j in range(d):
            Lambda_B[j] = 2*v / ( np.sqrt(Lambda_hat[j] + 10*c*v / beta * np.sum(np.sqrt(Lambda_hat) + 10*c*v / beta)) )

        Sigma_B = np.dot(U_hat, np.dot(np.diag(1.0 / Lambda_B), U_hat.T))

    else:
        Sigma_B = (np.sum(Lambda_hat) + d*c) / (2*v) * np.eye(d)

    return Sigma_B

#Define Mechanism M (X --> Y)
def M(X):
    #for ease of testing, let M = I
    return X

#Define distribution D of rv X
def distrib():
    #for ease of testing, let D be uniform
    return np.random.uniform(0,1)
    

m = 100  #Sampling complexity (number of data points sampled)
c = 0.1  #Security parameter
v = 0.5  #Mutual information quantity
beta = 0.01  #Mutual information quantity
r = 0.1 #some parameter

#(1-gamma)-Confidence noice Determination of Deterministic Mechanism M 
cov_mat = noise_determination(M, distrib, m, c, v, beta)
print(cov_mat)


