---
title: The art of readable code
date: 2021-10-08
tags: ['book', 'the_art_of_redable_code']
draft: false
summary: 
---
-   Overall metric for readability: 
	-   code should be written to minimize the time it would take someone else to fully understand it (able to modify the code and spot bugs) 
	-   Below find the ways to improve readability (ranked from easiest change to most time intensive)

#### Naming of Variables / Functions / Classes:
- **GOAL** : 
	- Compact & Concrete 
	- Unambiguous 
	- Word formatting + Consistency
	
-   Use specific, descriptive, succinct names that say the entity's value or purpose

-   Use concrete names instead of abstract names
	-   serverCanStart -> canListenOnPort
-   Add important attributes e.g. units or state 
	-  url -->  unsafeUrl, safeUrl
-   Can use shorter variable names for smaller scope
-   Use word-formatting (e.g. camelCase, snake_case), check style guide
-   Avoid names that can be misunderstood 
	-   filter --> exclude, select 
-   Prefix `max`, `min` when defining upper and lower limits
-   Use `first` and `last` for inclusive ranges
-   Use `begin` and `end` for inclusive/exclusive ranges
-   Prefix `is/has/can/should` for boolean vars
	-   Ex: is_owner, can_deliver ... 
-   Use positive rather than negated terms
	-  disable_ssl = False --> use_ssl = True 

####  Aesthetics
- **GOAL** :
	- Aligned Code
	- Consistent style 	
	
-   Similar code should have similar silhouettes

-   Use line breaks to segment a block of code to increase high level understanding
-   Consider using column alignment
-   Consistency of style in the entire project is much more important than using the right style. 

####  Commenting
- **GOAL** :
	- Be empathetic 
	- Get rid of assumptions
	- Good comment is not meant to explain bad code. ( Fix the code )
	- Director comments (```FIXME, TODO, HACK, XXX```)
	- Avoid pronouns 
	- Good comment acts as redundancy check, kind of like a Unit test. 
	- A precises example is better than a lengthy comment. 
	- Use words that pack a lot of meaning. 
	
-   Can be 
	-   High level / "big picture" explanation of what code is doing
	-   Record of your thought process when writing the code
	-   Explanation for potential "huh?" moments
	-   Director comments e.g. instructions for future code user
		-   Consider using `TODO` / `FIXME` / `HACK` / `XXX`
	-   Warning for surprising behaviors
	-   Example input/output of a function

- Avoid:
	-   Unclear pronouns, _what does "it" refer to?_
	-   Repeating the function definition in prose form
	-   Stating what is literally being done

#### Making control flow easier to read
- **GOAL** :
	- Make the control flow so natural that the user doesn't have to stop and reread the code. 
	- Prioritize time needed to understand the code over minimizing number of line.
	- Use summary variables for expressions used in conditions for easy understanding. 
	- Break down giant statements / expressions 

-   Order of arguments in conditionals:
	-   LHS = Expression being changed / interrogated
	-   RHS = Expression that is constant or being compared to

-   Use ternary operations only for simple cases
-   Use `while` loops instead of `do/while` loops
-   Avoid many layers of nesting as it becomes hard to maintain a mental image of the conditionals. Choose to refactor or return early instead

-   Viable and different `if/else` ordering philosophies:
	-   Deal with positive case first
	-   Deal with simpler case first (good to reduce LOC between `if` and `else`)
	-   Deal with most relevant/interesting case first

-  Summary Variables 
    -   Introduce "explaining variables" to capture a sub expression (rather than use raw logic)
    -   Use "summary variables" to summarize logic e.g.
        
	```
	if(request.user.id != document.owner_id) ... 

	changed to


	boolean user_owns_document = request.user.id == document.owner_id

	if (user_owns_document) ...
	```

-   When dealing with complex logic, sometimes approaching the inverse goal can simplify implementation


#### Variables & Readability 
- **GOAL** :
	
	- Eliminate temporary variables by returning early / dealing immediately. 
	- Shrink the scope of variables so the reader has few things to remember. 
		-   Try passing in arguments instead
		-   Try breaking down a complex class
		-   Try making methods static
	- Prefer "write-once" variables whose values don't change too often so that it is easier to reason its value


- Remove variables that don't serve any purpose. 
	- Does not give any clarification 
	- Does not break down a large expression / statement 
	- Used only once 
- The sole purpose of Modularity is to isolate purpose & data i.e variables. 
- In Python variables defined in a block like if/for spill out unlike in C (Scoping rule).
- Move variables to the respective block of code where they are used rather than defining all variables on top of function. 


#### Refactor; Extract unrelated sub problems from a method implementation
- **GOAL** :
	- Modularity 
	- Reuse 
	- Better high level picture. 
	
-   Separate generic code from project specific code

-   Generate code can usually go into a `utils` folder / collection of helpful and frequently used methods
-   Pros of separating logic:
	-   Allows reader to focus on high level goal without being bogged down by implementation detail
	-   Allows separated functions to be reused
	-   Easier to test isolated logic
	-   Easier to identify edge cases


#### One task at a time 
- Organize your code to perform once task at a time. 


#### Turn thoughts to code 
- You do not really understand unless you can explain it your grandmother --Albert Einstein 
- Use rubber ducking concept, sometimes when you listen to yourself you will understand how smart / dumb you sound. 


####  Write less code
-   Rethink requirements for a function to solve the easiest version of the problem

-   Don't get over excited, implement crucial and necessary code first ( Lean strategy ). 
-   Don't be too optimistic in estimating time to code. 
	-   Think time 
	-   Code time
	-   Document time
	-   Maintenance time
	-   Refactor time
	-   Optimize time. 
- Stop making it 100% perfect, you don't need to handle every possible input. ( Rethink requirement )
-   Familiarize yourself with (standard) libraries and the available methods
	-  A lot of times programmers aren't aware that existing library could solve their problem --> Periodically spend 15 minutes getting familiar with the standard libraries. 
-   Handle vital / frequent cases first.
-   Many times UNIX command tools could replace hundreds of lines of code and much more efficient. 


#### Weight of the project 
-   Be conscious of the weight of the project, ruthlessly prune unused code

-   Remove unused code / useless features / libraries 
-   Remove duplicated code by creating generic utility code. 
-   Compartmentalize into disconnected sub projects 
-   Keep your code base light. 
-   Library size vs Its Use 


#### Making test code more readable
-   Print better error messages e.g. include the input, output and expected output, where applicable (some assertion libraries might have this functionality)

-   Choose test cases that are both simple and effective in exposing potential bugs
-   Break down these test cases into smaller ones to introduce granularity (facilitates debugging later on)
-   Pick good names e.g. Test__


#### Try test-friendly development maybe?
-   Code functions that
	-   Have a well defined interface
	-   Have little to no "set up"
	-   Have no hidden data to inspect

#### Lastly
-   Avoid

	-   Non constant global vars as they have to be reset for each test case and it is hard to determine which functions have side effects
	-   Code that depends on a lot of external components as this increase amount of set-up needed for testing and increased dependency introduces more points of failure in code
	-   Code with non-deterministic behavior as this is difficult to test and is probably susceptible to race conditions and non-reproducible bugs
	
-   Try to have
	-   Classes that have little to no internal state so there is little to no set up and is simpler to understand
	-   Classes/functions that does only one thing so that fewer tests are needed to fully test it and it is indicative of a decoupled system
	-   Classes/functions that are highly decoupled so that they can all be developed, modified and tested independently/in parallel.
	-   Functions that have well defined interfaces so that what to test becomes clear and function can be easily understood and reused elsewhere


#### Benefits of readable code

-   Easier to spot bugs
-   Easier to onboard new developers on team (or could be you revisiting the code in 6 months)
-   Easier to make changes to code
-   Easier to maintain


---

Author: Dustin Boswel , Trevor Foucher 

Status: #done

Tags: 
#book
#the_art_of_redable_code

References:

Related:

