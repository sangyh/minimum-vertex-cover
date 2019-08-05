# minimum-vertex-cover
Algorithms course project to implement branch and bound algorithm on minimum vertex cover problem. 

The MVC problem seeks the smallest set of vertices such that every edge in the graph has at-least one endpoint in it, thereby forming the MVC solution.The BnB algorithm is an exact technique that systematically traverses the search space evaluating all options.

The report describes four distinct approaches, including an exact solution implemented using the Branch and Bound (BnB) technique, an approximation algorithm using Greedy Independent Cover and two local search algorithms including Hill-Climbing and Simulated
Annealing are considered. Their performance is tested on real and random datasets extracted from the 10th DIMACS challenge, and evaluated for accuracy and computational effeciency. As expected from theoretical understanding of the algorithms, we saw that the BnB algorithm was slow in running time while being fairly accurate while the approximation algorithm was quick but with a higher relative error. Interestingly, the Local Search algorithms, which were cleverly designed to accept the heuristic solution as a initial starting point,showed a very good performance within the default cutoff running time of 600 seconds, also nding the optimum solution in most cases.

I implemented the BnB solution, while my two other teammates implemented the approximate and local search solutions.
