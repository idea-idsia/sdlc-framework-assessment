**Answer to the first question**

Let  

\[
X=\{x_{1},x_{2},\dots ,x_{n}\}\subset \mathbb R^{d}
\]

be the set of points that are to be clustered.  
For a partition \(P=\{C_{1},\dots ,C_{k}\}\) of \(X\) define the *within–cluster
sum of squares* (WCSS)

\[
\operatorname{WCSS}(P)=\sum_{j=1}^{k}\;\sum_{x\in C_{j}}\|x-\mu _{j}\|^{2},
\qquad 
\mu _{j}=\frac{1}{|C_{j}|}\sum_{x\in C_{j}}x .
\]

The **k‑means objective** is

\[
\min_{P}\operatorname{WCSS}(P).
\]

The *k‑means algorithm* ( Lloyd’s algorithm) is an iterative
procedure that alternates two steps:

1. **Assignment step** – given the current cluster centres
   \(\{\mu _{1},\dots ,\mu _{k}\}\) assign every point to the nearest centre:
   \[
   C_{j}\leftarrow \{x\in X:\|x-\mu _{j}\|^{2}\le
   \|x-\mu _{l}\|^{2}\;\forall l\}.
   \]

2. **Update step** – recompute each centre as the mean of the points
   that have been assigned to it:
   \[
   \mu _{j}\leftarrow \frac{1}{|C_{j}|}\sum_{x\in C_{j}}x .
   \]

The assignment step keeps the centres fixed and therefore can only
decrease (or leave unchanged) the objective value, because each point
is moved to the cluster whose centre is closest to it.  
The update step keeps the assignment fixed and again can only
decrease (or leave unchanged) the objective value, because the mean of
a set of points is the point that minimises the sum of squared
distances to that set.

Consequently the objective value is non‑increasing at every
iteration.  Because the objective is bounded below by zero, the
sequence of objective values converges.  The algorithm terminates
when the assignment no longer changes (or when the change in the
objective is below a prescribed tolerance).  At that point the
partition is a **local optimum** of the k‑means objective: moving any
single point to a different cluster or changing any centre cannot
reduce the objective further.

Thus the k‑means algorithm is guaranteed to converge to a local
minimum of the within‑cluster sum of squares.

---

**Answer to the second question**

The k‑means objective is a *continuous* function of the data points
\(X\).  Small perturbations of the points produce small changes in the
objective value.  However, the algorithm is **not** a continuous
mapping from the data to the final partition.  A tiny change in a
single point can cause a different point to be assigned to a
different cluster, which in turn can change the centres and the
entire subsequent sequence of assignments.  Because the algorithm
searches a discrete space of partitions, the mapping from data to
cluster labels is discontinuous.

Therefore, while the objective function is continuous, the
k‑means algorithm itself is **not** continuous in its output with
respect to its input.