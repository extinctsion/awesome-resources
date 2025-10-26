# How to Write Pseudocode in English

**Pseudocode** is a simplified, language-agnostic way of writing algorithms. It's written in plain English (or near-English) to describe the steps a program should take --- without worrying about syntax.

Why Write Pseudocode?
---------------------

Writing pseudocode helps you:\
- Clarify your thought process before coding.\
- Focus on what needs to be done, not how it's implemented.\
- Communicate ideas with others who may not know the programming language.\
- Detect logical errors early.

Basic Rules of Writing Pseudocode
---------------------------------

- Write in simple, structured English.

- Capitalize keywords (optional but helps readability).

- Indent blocks to show hierarchy and nesting.

- Use meaningful variable names.

- Avoid syntax from real programming languages.

Common Pseudocode Keywords
--------------------------

| Keyword                        | Meaning                        |
| ------------------------------ | ------------------------------ |
| **START / END**                | Begin and end of the algorithm |
| **INPUT**                      | Get data from user             |
| **OUTPUT**                     | Display data to user           |
| **SET / INITIALIZE**           | Assign a value                 |
| **IF / ELSE / END IF**         | Decision-making                |
| **FOR / WHILE / REPEAT UNTIL** | Loops or repetition            |
| **CALL**                       | Invoke a procedure or function |
| **RETURN**                     | Output a value from a function |

Example 1: Find the Sum of Two Numbers
--------------------------------------

**START**
    INPUT number1
    INPUT number2
    SET sum = number1 + number2
    OUTPUT 'The sum is', sum
**END**

Example 2: Find the Largest of Three Numbers
--------------------------------------------

**START**
    INPUT a, b, c
    IF a > b AND a > c THEN
        OUTPUT 'A is the largest'
    ELSE IF b > a AND b > c THEN
        OUTPUT 'B is the largest'
    ELSE
        OUTPUT 'C is the largest'
    END IF
**END**

Example 3: Loop Through a List
------------------------------

**START**
    SET total = 0
    FOR each number in list
        SET total = total + number
    END FOR
    OUTPUT 'Total sum =', total
**END**

Tips for Writing Good Pseudocode
--------------------------------

- Keep it short, clear, and structured.
- Don't include unnecessary technical details.
- Focus on logic flow --- not syntax.
- Use indentation and blank lines for readability.
- Add comments to explain tricky steps.

Summary
-------

Writing pseudocode in English helps bridge the gap between thinking and coding. It's especially useful for:\
- Planning algorithms\
- Writing documentation\
- Explaining code logic during interviews\
- Collaborating with non-programmers

***Good pseudocode should make sense to any human, even without code knowledge***