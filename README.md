# Islands
Galapagos Islands exercise

A group of botany students is interested in innovation. To achieve that, they decide to take a trip to Wolf Island (one of the Galapagos Islands that can only be visited for research purposes or professional diving, not for tourists). This trip is naturally very expensive, so they must make the most of it. They plan to investigate a new species of insect that lives in the treetops, but since the island is over 1.5 square kilometers in size, they need to maximize the sampling process. The sampling process is organized into n zones distributed across the island, where each zone has an expected quantity of insects to collect, denoted as i.

The idea is to receive a list of the n expected quantities of insects per zone and construct a binary tree in level order. During the construction of this tree, values in the range [-1, 25] will be encountered. The value -1 is used to represent NULL, indicating that the corresponding node does not exist and cannot be included in the expedition. The other values, different from -1, represent the expected quantities of insects.

The expedition starts at the crater of Wolf volcano, which is the first zone in the given list and represents the root of the previously created binary tree. Due to limited resources, they can only visit a nodes in the tree. Therefore, one of the students proposes three ways to perform the expedition: inorder, preorder, and postorder traversal. The student suggests visiting the first a nodes in each traversal, but they don't have a computer on the island to perform the calculations.

Your mission is to help the student find the best traversal (inorder, preorder, or postorder) and determine the maximum expected quantity of insects they can collect during that traversal.

Please note that if two traversals have the same number of expected insects, the following preference criteria should be applied: Preorder - Inorder - Postorder.

Constraints

The input binary tree is a complete binary tree with levels ranging from 3 to 12.
The values of each node range from 0 to 25, with the restriction that -1 represents NULL.

Input

The first line contains the sorted list of possible insects per zone (the first element represents the root of the tree). There are enough elements in the list to construct a complete binary tree at its last level. The second line contains the number of nodes to be visited.

Output

The output starts with the best traversal to perform, with the first letter capitalized ("Preorder", "Inorder", "Postorder"). Separated by a space, the maximum quantity of insects that can be collected during the expedition is provided.

The main.py file solve this problem when is run.
