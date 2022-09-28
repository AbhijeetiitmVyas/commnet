<img src="others/images/purdue-cs-logo.jpg" alt="drawing" width="450"/>

# Things to Expect and Do When Reading and Reviewing a Paper

> **Note:** These are from my Ph.D. advisor, Jen Rexford's [class](https://www.cs.princeton.edu/courses/archive/fall20/cos461/561.html).

Everyone is expected to know and be prepared to discuss the following 8 things about each paper.

1. What problem is it solving?
2. Why is that problem important?
3. What was the previous state-of-the-art?
4. How (and how much) does this paper advance the state-of-the-art?
5. How does the protocol, system, or design work?
6. What are the key insights in the design that enabled it to advance the state-of-the-art?
7. How is the design evaluated, and what are the key results?
8. What related problems are still open, and is this problem fully solved?

Most papers give you an answer to each of these questions. Do not immediately act that answer! Think about each of these questions for yourself. Consider the background you've gained in lectures, previous discussions, and elsewhere. What do you think the **right** answer is for each of these questions? Rarely is it exactly what the authors wrote.

In addition, everyone is expected to be able to make a substantial contribution to our discussion of the paper beyond those eight things. Here are a few ideas about what to think about so you can make such a contribution.

### a. Follow-On Research

What would your follow-on research to this paper be?  For example, improve an algorithm in the paper. Include a rough evaluation (see below). This is the category you will almost always naturally fall into when reading a paper! Virtually reimplementing the work based on the problem and goals will almost always lead to a good one of these!

### b. Generalizer | Specializer
Can you generalize what the paper is doing so your sketch of a design can do a strict superset of what the paper does, while still being mostly as efficient?  Or, can you specialize what the paper is doing so your sketch of a design can do a strict subset of what the paper does, but does it more efficiently?  (Explain why it's a specialization/generalization, explain why we care about it, explain how your design would differ for it, explain what your design would do better, and explain why specifically it would realize that improvement). Include a rough evaluation (see below).

### c. Evaluator
What would the ideal evaluation of this design look like? How close did their evaluation come? What one more experiment should they have run? Come up with your ideal evaluation BEFORE you read their evaluation and then compare! Must include rough evaluation (see below). Do this only for the most important experiment that wasn't run and explain why that's the most important one.

### d. Rough Evaluation
Describe one (or at most two) experiments. Why did you choose this experiment, i.e., why is it the most important 1 (or 2). What results do you expect to see And WHY! Higher throughput for X is the result; why will the throughput be higher? Be very explicit about this!

### e. Connector
Connect this paper to a previous paper we have read this semester. You could compare/contrast. You could use an idea from an earlier paper here. You could use an idea from this paper in an earlier paper. You could try porting this paper to the earlier papers' setting, or vice versa.
