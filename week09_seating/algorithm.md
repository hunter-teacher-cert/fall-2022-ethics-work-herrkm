# Original Concept

My own original idea was operating under the assumption that the economy plus policy 
would remain in place. I would have revised only the regular economy portion of the algorithm,
in which I would have had the algorithm seat groups of 3 first by searching for 3 adjacent seats.
If 3 adjacent seats could not be found, I would search for a pair with a single seat in an
adjacent row. Only if such a situation could not be found would I resort to random seating.

However, upon discussion with group members, we decided to do away with the economy plus policy
to simplify the process and reduce the inherent unethical nature of the policy, with the 
general idea that later bookers would get a discount. We also decided, based on Will's
research into actual booking patterns, to change the party sizing so that parties were 50% 
individual, 25% pairs, and 25% groups of 3 For simplicity, however, the algorithm
implemented takes the dictionary of purchasers and seats groups of 3 first, front to back
and left to right. If the group of 3 is impossible to seat together, it searches for a single
seat immediately behind. Then, pairs are seated similarly (together if possible, adjacent rows
otherwise),and finally individuals are filled in where room allows.
