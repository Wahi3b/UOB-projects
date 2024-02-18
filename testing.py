

def cluster(x,K,R):
    import math
    import random
    # Find minimum of list of tuples
    def mintuple(x):
        xmin = math.inf
        for i,xp in x:
            if xp < xmin:
                imin,xmin = i,xp
        return (imin,xmin)

    # Ensure cluster assignment is feasible (has at least one data point in each cluster)
    def cluster_fix(X,K):
        N = len(X)
        for k in range(K):
            if X.count(k) == 0:
                X[k] = k
        return X

    # Cluster means
    def cluster_means(x,X,K):
        N = len(X)
        mu = [0]*K
        for k in range(K):
            xk = [x[i] for i in range(N) if X[i]==k]
            mu[k] = sum(xk)/len(xk)
        return mu

    # Compute cluster objective
    def cluster_obj(x,X,mu,K):
        N = len(X)
        F = 0
        for k in range(K):
            xk = [x[i] for i in range(N) if X[i]==k]
            dk = sum([(xp-mu[k]/len(xk))**2.0 for xp in xk])
            F = F + dk
        return F

    # Create 1-Hamming distance cluster assignment neighbourhood
    def cluster_nbr(X,K):
        N = len(X)
        Xnbr = []
        for n in range(N):
            j = X[n] + 1
            if j == K:
                j = 0
            Xn = X.copy()
            Xn[n] = j
            Xnbr = Xnbr + [cluster_fix(Xn,K)]
        return Xnbr

    # Evaluate objectives for cluster assignment neighbourhood
    def cluster_nbrobj(x,Xnbr,K):
        N = len(x)
        Fnbr = []
        for nbr in range(N):
            mu = cluster_means(x,Xnbr[nbr],K)
            Fnbr = Fnbr + [(nbr,cluster_obj(x,Xnbr[nbr],mu,K))]
        return Fnbr
    # Step 1. Initialization

    # Start with random cluster assignments
    N = len(x)
    X = []
    for n in range(N):
        X = X + [random.randint(0,K-1)]
    X = cluster_fix(X,K)
    n = 0
    while (n <= R):

        # Step 2. Neighbourhood search and termination check

        # Compute current cluster objective
        μ = cluster_means(x,X,K)
        F = cluster_obj(x,X,μ,K)
        print(f'Iteration n={n}: assignments X={X}, objective F={F}')

        # Find (1-Hamming) neighbourhood of cluster assignments
        Xnbr = cluster_nbr(X,K)

        # Evaluate objective value of all cluster assignments in neighbourhood
        Fnbr = cluster_nbrobj(x,Xnbr,K)

        # Select optimal assignment X in neighbourhood
        iopt,Fopt = mintuple(Fnbr)

        # Check termination
        if Fopt >= F:
            break

        # Update assignments
        X = Xnbr[iopt]

        # Step 3. Iterate
        n = n + 1
    
    return X,F
x = [0.1,-0.3,2.6,1.1,2.3,-0.8,-6.2,-7.8,-1.5,-0.4]
print(f'Input data: x={x}')
K = 3
R = 20
Xopt,Fopt = cluster(x,K,R)
print(f'Greedy K-clustering: X*={Xopt}, F*={Fopt}')