Constraint satisfaction problems (CSP) - Map Coloring
A -coloring of a map is an assignment of colors, one to each country, in such a way that no two countries sharing a border have
the same color. This problem can be translated to a constraint graph. A coloring of a graph G assigns a color to each vertex of G,
with the restriction that two adjacent vertices never have the same color. The chromatic number of G, written χ(G), is the smallest
number of colors needed to color G.
In this project, we will experiment with map coloring techniques and compare the observed results in the context of USA and
Australia maps.
Compute the chromatic number of USA and Australia map.
Experiment with both maps using the following methods [without heuristics]
Depth first search only
Depth first search + forward checking
Depth first search + forward checking + propagation through singleton domains
Experiment with both maps using the following methods with heuristics where the order of variables needs to be defined in
the following order MRV, Degree Constraint, and Least Constraining Value
Depth first search only
Depth first search + forward checking
Depth first search + forward checking + propagation through singleton domains
Present the results in a tabular format
the number of backtracking happened and
the time required to compute the result.
General instructions:
1. The project can be completed individually, or in a group of three max.
Many students work alone, which is good. If you prefer to work in a group, you are responsible for making your own
group.
2. Map visualization is preferred but not required. For visualization you can use any framework or tool.
Submission instructions:
1. Your program should be well documented, and you should turn in the following to canvas.
An external document describing the map coloring problem formulation, the program structure, global variables, the
function/procedure to compute the heuristic function, and other functions/procedures, etc.
Your program source codes (with necessary inline documentation);
The execution results as specified above.
Each member must turn in everything in canvas.
2. 10% late submission penalty for each extra day. Cut-off: Three days after the deadline.
Warning: Any form of cheating will subject you to disciplinary act.
--------------------
Here is a guideline to experiment with map coloring algorithms.
Without Heuristics
1. Define the order of states randomly for map coloring
2. Run the following algorithms for the same random order of states
Depth first search only
Depth first search + forward checking
Depth first search + forward checking + propagation through singleton domain
3. Repeat steps 1 and 2 at least four times.
4. Show the results in a table for both maps
With Heuristics
1. Start with a state
2. Run the following algorithms - this time, you will use heuristics to select next variable and value where appropriate at
runtime
Depth first search only
Depth first search + forward checking
Depth first search + forward checking + propagation through singleton domain
3. Repeat steps 1 and 2 at least four times.
4. Show the results in a table for both maps
Compare all results and analyze them.
