import numpy as np

def noise_determination(M, D, m, c, v, B):
    #Lines 2-5
    y_labels = np.zeros(m)
    for k in range(m):
        X_k = D()
        y_labels[k] = M(X_k)
    
    #Line 6
    mu_hat = np.mean(y_labels)
    Sigma_hat = np.cov(y_labels, rowvar=False)

    #Line 7
    U_hat, Lambda_hat, _ = np.linalg.svd(Sigma_hat)
    d = len(Lambda_hat)

    #line 8
    j0 = np.argmax(Lambda_hat > c) #I'm concerned because Lambda should not be 1d here right?
    print("Debug: j0", j0)

    #Lines 9-16
    if np.min([np.abs(Lambda_hat[i] - Lambda_hat[j]) for i in range(j0+1) for j in range(d)]) > r * np.sqrt(d*c) + 2*c:
        Lambda_B = np.zeros_like(Lambda_hat)
        for j in range(d):
            Lambda_B[j] = 2*v / ( np.sqrt(Lambda_hat[j] + 10*c*v / beta * np.sum(np.sqrt(Lambda_hat) + 10*c*v / beta)) )

        Sigma_B = np.dot(U_hat, np.dot(np.diag(1.0 / Lambda_B), U_hat.T)) #I'm concerned that this is not how you take the inverse of Lambda

    else:
        Sigma_B = (np.sum(Lambda_hat) + d*c) / (2*v) * np.eye(d)

    return Sigma_B



# Define your mechanism M, data distribution D, and parameters
def M(X):
    # Your deterministic mechanism implementation here
    pass

def D():
    # Your data distribution sampling implementation here
    pass

d = 10  # Dimensionality of the output
m = 100  # Sampling complexity
c = 0.1  # Security parameter
v = 0.5  # Mutual information quantity
beta = 0.01  # Mutual information quantity
r = 0.1  # Parameter r

# Call the function
result = noise_determination(M, D, m, c, v, beta, r)
print(result)
