# Hints

**Problem 1**: Ensuring an equal number of left and right brackets is trivial. To ensure that brackets are closed in the right order we use a stack. Parse the string left to right, pushing all left brackets to the stack. When we hit a right bracket, it must match the most recent unclosed left bracket.

**Problem 2** 

Here's an example with a single valid substring in bold:

 <span style="font-size: 1.5em;">( ( ( **( ) ( )** ( ( ( </span>

 Clearly, this substring has a length of 4. Correctly counting the maximum length relies on three points of intuition:

 1. A valid sub-string always ends with a ")" character.

 2. We count the length of a valid substring by counting back from its end to either the closest unmatched openning parenthesis (this is the case in the example), the beginning of the string, or the end of the most recent invalid substring.

 3. We can condense these three possibilities into one by imagining an extra "(" at the beginning of the string and after each invalid substring.

 Here's the outline of the algorithm using stacks:

 1. Create a stack to store the indices of all the left parentheses in the string.

 2. Create a "ghost parenthesis" by pushing `-1` to the stack.

 3. Traverse the string character-by-character.
     
     - If the character is an opening parenthesis, push its index to the stack

    - If the character is a closing parenthesis, pop the stack.

      - If the stack is empty, we've popped the ghost parenthesis--the current substring is invalid! Insert a new ghost parenthesis by pushing the current index to the stack.

      - If the stack is not empty, then the length of substring is the distance from the current index to the index on top of the stack.

**Problem 3**

Use [Dijkstra's Two-Stack Algorithm](https://switzerb.github.io/imposter/algorithms/2021/01/12/dijkstra-two-stack.html).
