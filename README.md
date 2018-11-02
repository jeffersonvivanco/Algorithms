# Algorithms 
Notes from the book Grokking Algorithms by Aditya Y. Bhargava.

These are intro notes to algorithms. I feel like my algorithm notes are all over the place, in paper, my computer, in the back of my head, so I'm putting it all here for reference. 

## Intro to Algorithms
### Binary Search
* Binary Search
    * For any list n, binary search will take logbase2 n steps to run in the worst case whereas simple search will take n steps. Binary search runs in logarithmic time.
    * log reference
        * 2^3 = 8 <-> logbas2 8 = 3. (In other words, how many 2s do we multiply together to get 8).
        * In algorithms, log always means logbase2
    * Binary search only works when your list is sorted.

### Big O Notation
* Big O notation tells you how fast an algorithm is. Big O notation lets you compare the number of operations. For example, lets say you have a list of size of n. Simple search checks each element so it will take n operations. The run time in Big O notation is O(n)
* Big O establishes a worst-case run time
* Some common Big O run times. Here are 5 big O run times that you'll encounter a lot, sorted from fastest to slowest:
    * O(log n), aka log time, gets faster as the list grows, ex: binary search
    * O(n), aka linear time, ex: simple search
    * O(n * log n), ex: a fast sorting algorithm like quicksort
    * O(n^2), a slow sorting algorithm like selection sort
    * O(n!), a really slow sorting algorithm, like the traveling salesperson
* **Important** Algorithm speed isn't measured in seconds, but in growth in the number of operations.

## Sort
* Arrays
    * Using an array means all your items are stored contiguosly in memory.
    * Since items are stored contiguosly, if you add a new item and there is no more room in memory, the array has to be moved to a new spot in memory to accomodate the new item, this can make adding a new item slow.
    * You can allocate space in advance but then
        * you may not need the extra space you asked for and since no one else can use it, this space is wasted
        * you may add more items then the space you allocated so the array will have to move to a new spot anyways
* Linked Lists
    * Linked lists solve the space problem that arrays have by storing items in scattered memory locations
    * With linked lists, your items can be anywhere in memory. Each item stores the address of the next item in the list. A bunch of random memory addresses are linked together.
    * Adding an item to a linked list is easy: you stick it anywhere in memory and store the address with the previous item. 
    * Reading items
        * Suppose you want to read the last item in a linked list. You can't just read it, because you don't know what address it's at. Instead you have to go to item #1 to get the address for item #2. Then you have to go to item #2 to get the address for item #3. And so on, until you get to the last item.
    * Linked lists are great if you're going to read all the items one at a time. But if you are going to keep jumping around, linked lists are terrible.
    * Arrays are different. You know the address for every item in your array ex: index starts at 0 so the first element is at index 0, third element at index 2, and so on. 
* Inserting into the middle of a list
    * What's better if you want to insert elements in the middle: arrays or lists?
        * With lists, it's as easy as changing what the previous element points to.
        * But for arrays, you have to shift all the rest of the elements down. And if there is no space, you might have to copy everything to a new location. Lists are better if you want to insert elements into the middle.
* Deletions
    * Lists are better, because you just need to change what the previous element points to. With arrays, everything needs to be moved up when you delete an element.
    * Unlike insertions, deletions will always work. Insertions can fail sometimes when there's no space left in memory. But you can always delete an element.
* Run times for common operations on arrays and linked lists

    |           |  Arrays | Lists |
    | -:        |-:       | -:    |
    | Reading   | O(1)    | O(n)  |
    | Insertion | O(n)    | O(1)  |
    | Deletion  | O(n)    | O(1)  |
* It's worth mentioning that insertions and deletions are O(1) time only if you can instantly access the element to be deleted. It's a common practice to keep track of the first and last items in a linked list, so it would take only O(1) time to delete those.
* Which are used more?
    * Arrays see a lot of use because they allow random access.
    * There are two different types of access: *random access* and *sequential access*.
        * Sequential means reading the elements one by one. **Linked Lists can only do sequential access.**
    * Arrays are faster at reads because they provide **random access**.

## Recursion
* Recursion is when a function calls itself.
* Recursion is used when it makes the solution clearer. 
* **There is NO performance benefit to using recursion; in fact, loops are sometimes better for performance. 
* When you write a recursive function, you have to tell it when to stop rrecursing. That's why every recursive function has two parts: *the base case, and the recursive case*.
    * The recursive case is when the function calls itself.
    * The base case is when the function doesn't call itself again ... so it doesn't go into an infinite loop.
* All function calls go onto the call stack.
* The call stack can get very large, which takes up a lot of memory.

## Divide and Conquer
* D&C algorithms are recursive algorithms.
* To solve a problem using D&C, there are two steps.
    * Figure out the base case. This should be the simples possible case.
    * Divide or decrease your problem until it becomes the base case.
* Euclid's Algorithm
* When you are writing a recursive function involving an array, the base case is often an empty array or an array with one element. If you are stuck, try that first.

## Sneak peek at functional programming
* "why would I do this recursively if I can do it easily with a loop?" you may be thinking. Well, this is a sneak peek into functional programming! Functional programming languages like Haskell don't have loops, so you have to use recursion to write functions like this. 

## Quicksort
* Used frequently in real life, for example, C has a function called qsort(), which is an implementation of quicksort
* Quicksort also uses D & C.
* Let's use quicksort to sort an array.
* Empty arrays and arrays with just one element will be the base case. You can just return these arrays as is, there is nothing to sort.
* Now, let's do an array with 3 elements. Remember, you are using D & C, so you can break it down until you're at the base case. 
* Here's how quicksort works
    * First, pick an element from the array. This element is called the pivot.
    * Now find the elements smaller than the pivot and the elements larger than the pivot. This is called partitioning. Now you have.
        * A sub array of all the numbers less than the pivot.
        * The pivot
        * A sub array of all the numbers greater than the pivot.
    * The two sub-arrays aren't sorted. They're just partitioned.
    * If the sub arrays are sorted, then you can combine the whole thing and the array is sorted.
    * If they are not sorted? Well, the quicksort base case already knows how to sort of arrays of two elements (the left sub-array) and empty arrays(the right sub-array). So, if you call quicksort on the two sub arrays and then combine the results, you get a sorted array.


## Inductive Proofs
* Inductive proofs are one way to prove that your algorithm works. 
* Each inductive proof has two steps, the base case and the inductive case.

## Merge sort vs Quicksort
* Worst case quicksort takes O(n^2) (as slow as selection sort) time and average O(nlogn) time. Merge sort takes O(nlogn) time worst case and average case. 
* So, you might be thinking, isn't merge sort faster since it takes O(nlogn) all the time?
* Well ... no, you see in big O notation, O(n) really means O(c * n)
    * c is some fixed amount of time that your algorithm takes.  Its called the *constant*.
    * It could vs 10ms * n or even 1s * n.
    * You usually ignore that constant, because if two algorithms have different big O times, the constant doesn't matter.
    * For example, let's say binary search and simple search had these constants: simple => 10ms * n, binary => 1sec * logn
    * You might say that simple search is much faster since it has a constant of 10ms. Now, lets suppose we search a list of 4 billion elements. Here are the times:
        * simple search => 10ms * 4 billion = 463 days
        * binary search => 1sec * 32 = 32 seconds
    * As you can see, binary search is way faster. And the constant made no difference.
    * Sometimes though, the constant can make a difference, like in quicksort and merge sort. Quicksort has a smaller constant than merge sort. So, if they are both take O(nlogn) time, then quicksort is faster. And quicksort is faster in practice because it hits the average case way more often than the worst case.
* Average case vs Worst Case
    * The performance of quicksort heavily depends on the pivot you choose.
    * Suppose you always choose the first element as the pivot. And you call quicksort with an array that is already sorted. Quicksort doesn't check to see whether the input array is already sorted. So it will still try to sort it.
        * **insert image here**
        * If you can visualize what quicksort is doing, you'll notice how you are not splitting the array into two halves. Instead, one of the sub-arrays is always empty. So the call stack is really long.
    * Now instead, suppose you always picked the middle element as the pivot. 
        * **insert image here**
        * You'll notice that the call stack is short. Because you divide the array in half every time, you don't need to make as many recursive calls. You hit the base case sooner, and the call stack is much shorter.
    * The first example (first element as pivot) is the worst case scenario, and the second example (middle element as pivot) is the best case scenario. In the worst case, the stack size is O(n). In the best case, the stack size is O(logn).
    * **Now look at the first level in the stack.** You pick one element as the pivot, and the rest of the elements are divided into sub-arrays. You touch all eight elements in the array. **So this first operation takes O(n) time. You touched all eight elements on this level of the call stack. But actually, you touch O(n) elements on every level of the call stack.**
        * **Even if you partition the array differently, you're still touching O(n) elements every time.**
        * **So each level takes O(n) time to complete.**
        * **In the best case scenario, there are O(logn) levels. And each level takes O(n) time. The entire algorithm will take O(n) * O(logn) = O(n logn) time.**
        * **In the worst case there are O(n) levels, so the algorithm will take O(n) * O(n) = O(n^2) time.**
    * **The best case is also the average case.** *If you always choose a random element in the array as the pivot, quicksort will complete in O(n logn) time on average.*

## Hash tables
* Hash functions
    * A hash function is a function where you put in a string (any kind of data, a sequence of bytes) and you get back a number.
    * Requirements for a hash function
        * It needs to be consistent. For example, suppose you put in apple and get back 4. Every tiime you put in apple you should get 4 back. Without this, your hash table wont work.
        * It should map different words to different numbers. For example, a hash function is no good if it always returns 1 for any word you put in. In the best case, every different word should map to a different number.
    * A hash function knows how big your array is and only returns valid indexes.
* A hash table is basically a hash function and an array together. It maps keys to values using a hash function. 
* **Hash tables are also known as hash maps, maps, dictionaries, and associative arrays. Hash tables are as equally fast as an array**.
* Use cases
    * Phone phonebook
    * Mapping a web address to an IP address
        * this process is called DNS Resolution.
        * hash tables are one way to provide this functionality
    * using hash tables as a cache
        * caching is a common way to make things faster. All big websites use caching. And that data is cached in a hash.
* Recap
    * Hashes are good for
        * Modeling relationships from one thing to another thing
        * Filtering out duplicates
        * Caching/memorizing data instead of making your server do work

### Collisions
* **Important** Above, it was stated that a hash function **always** maps different keys to different slots in the array, this is a **lie**. In reality, it's almost impossible to write a hash function that does this.
* When two keys map to the same slot, we have a **collision**.
* There are many different ways to deal with collisions. The simplest one is this: if multiple keys map to the same slot, start a linked list at that slot.
* To prevent a linked list from becoming too long, you need a good hash function. A good hash function maps all keys evenly all over the hash, this way there are few collisions making your linked list not too long.

### Performance
|           |  Hash Tables (avg.) | Hash Tables (worst) | Arrays | Linked List |
| -:        |-:                   | -:                  | -:     | -:          |
| Search    | O(1)                | O(n)                | O(1)   | O(n)        |
| Insert    | O(1)                | O(n)                | O(n)   | O(1)        |
| Delete    | O(1)                | O(n)                | O(n)   | O(1)        |

* Avg time for hash tables is the best out of all those, but the worst time is also the worst one, so it's important that you don't hit worst case performance with hash tables. To do this, you need to avoid collisions.
* **To avoid collisions you need.**
    * a low load factor
    * a good hash function

* **low factor**: measures how many empty slots remain in your hash table.
    * to calculate => NumberOfItemsInHashTable/TotalNumberOfSlots
    * ex: Let's say we have a hash table with 3 slots and 1 item. Then the load factor is 1/3
    * Having a load factor greater than 1 means you have more items than slots in your array. Once the load factor starts to grow, you need to add more slots to your hash table. This is called *resizing*. To resize
        * First you create a new array that's bigger. The rule of thumb is to make an array that is twice the size.
        * Then you re-insert all of those items into this new hash table using the hash function.
    * After you have resized your hash table, you'll have a lower load factor. **With a lower load factor, you'll have fewer collisions, and your table will perform better**.
    * **A good rule of thumb is, resize when your load factor is greater than 0.7**.
    * You might be thinking, "This resizing business takes a lot of time!" And you're right. Resizing is expensive, and you don't want to resize too often. But averaged out, hash tables take O(1) even with resizing. 
* **A good hash function**
    * A good hash function distributes values in the array evenly.
    * A bad hash function groups values together and produces a lot of collisions.
    * look up SHA function, we could use it as our hash function

## Breadth-first search
* Breadth-first search allows you to find the shortest distance between two things. You can use breadth-first search to
    * Write a checkers AI that calculates the fewest moves to victory
    * Write a spell checker (fewest edits from your spelling to a real word--for example, READED -> READER is one edit)
    * Find the doctor closest to you in your network
* Shortest path problem - always trying to find shortest way to do something
    * the algorithm to solve these type of problems is breadth-first search
    * to solve a shortest path problem:
        * first you model the problem as a graph
        * then you solve the problem using breadth-first search

### What is a graph?
* A graph models a set of connections. Graphs are a way to model how different things are connected to one another.
* Each graph is made up of nodes and edges.
* A node can be directly connected to many other nodes. Those nodes are called its *neighbors*.

### Breadth-first search
* Breadth-first search is a different kind of search algorithm: one that runs on graphs. It can help to answer two types of questions:
    * Question type 1: Is there a path from node A to node B ?
    * Question type 2: What is the shortest path from node A to node B ?

### Implementing the graph
* We want to implement a graph in code that consists of several nodes and each node is connected to neighboring nodes.
* We'll use a hash table to map a node to all of its neighbors
* If a graph has nodes only pointing to them but no arrows from them to someone else then this is called a *directed graph*--the relationship is only one way.
* An undirected graph has no arrows and both nodes are each other neighbors.

### Implementing the algorithm
* First, we make a queue and add all the nighbors of the start vertex
* Then, while the search queue is not empty, enqeue a neighbor vertex from the search queue and check if this is the vertex we are looking for, if it is great, if not, add all of this vertex's neighbors to the search queue
* The algorithm will keep going until thew queue is empty
* Note: You also have to keep a list of the vertices you have already checked. This is to avoid checking a vertex more than once or going into an infinite loop.
* Loop at the sample breadth-first_search program at jeffersonvivanco.com in the projects section

### Running Time
* If you search your whole graph, that means you'll follow each edge, so the running time is at least O(number of edges)
* You'll also keep a queue of every vertex you'll search, and adding a vertex to the queue take O(1), doing this for every vertex will take O(number of vertices).
* BFS takes O(V + E)
    
## Dijkstra's Algorithm
### There are four steps to dijkstra's algorithm
1. Find the "cheapest" node. This is the node you can get to in the least amount of time.
2. Check whether there's a cheaper path to the neighbors of this node. If so, update their costs.
    1. The cost of a node is how long it takes to get to that node from the start.
3. Repeat until you've done this for every node in the graph.
4. Calculate the final path.

### Terminology
* Each edge in the graph has a number associated with it. These are called *weights*.
* A graph with weights is called a *weighted graph*.
* A graph without weights is called an *unweighted graph*.
* **To calculate the shortest path in an unweighted graph, use breadth-first search. To calculate the shortest path in a weighted graph, use dijkstra's algorithm.**
* Graphs can also have *cycles*. It means you can start at a node, travel around, and end up at the same node.
* An undirected graph means that both nodes point to each other. That's a cycle!
* With an undirected graph, each edge adds another cycle. Dijkstra's algorithm only works with directed acyclic graphs, called DAGs for short.

### Negative Weight Edges
* **you can't use Dijkstra's algorithm if you have negative weight edges.** Negative weight edges break the algorithm.
* if you want to find the shortest path in a graph that has negative-weight edges, use Bellman-Ford algorithm.

### Implementation
* Algorithm
    * while we have nodes to process
    * grab the node that is closest to the start
    * update costs for its neighbors
    * if any of the neighbor's costs were updated, update the parents too
    * mark this node processed

