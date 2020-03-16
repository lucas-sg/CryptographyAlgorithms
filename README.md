# Cryptography Algorithms
Basic cryptography algorithms implemented in Python.

* Coincidence index attack on shift cipher
* Kasiski's attack on the Vigenère cipher

---
## Coincidence index attack on shift cipher
In order to break the shift cipher I followed the idea proposed on page 14 of _Introduction to Modern Cryptography_. It consists of approximating a probabilistic amplitude index (*C*), or coincidence index, given by the relative frequency of each letter on the corresponding alphabet of the encrypted message (*C*).

$I = \sum p_i^2 = 0.075$

Knowing the index, one can calculate the relative frequency of each letter in *C* and, instead of adding the squared probabilities of each letter, multiply the [actual frequency (_p<sub>i</sub>_)](https://en.wikipedia.org/wiki/Letter_frequency) with the calculated one (*q<sub>j</sub>*) from *C*. In order to know which *p<sub>i</sub>* to multiply with each *q<sub>j</sub>*, one must *"rotate"* or *advance* the *j* index until the value of the sum of all products *p<sub>i</sub>q<sub>j</sub>* is approximately the one above.

*Note: I noticed that the result of the aforementioned formula is approximately 0.075 for both English and Spanish. I got frustrated trying to implement this until I noticed that what the book suggest as the reference value (0.065) isn't right. Or not at least according to [Wikipedia's letter frequency](https://en.wikipedia.org/wiki/Letter_frequency).*


---
## Kasiski's attack on the Vigenère cipher
There are multiple explanations of how the Kasiski attack works on a Vigenère cipher. But for those unfamiliar, it basically groups the encrypted text in multiple rows of the key's length, due to the fact that every *n* characters the shift is the same. That way, after piling every row on top of one another, each column will have the same shift and that shift will be easily deciphered by the aforementioned method by analysing each column. Now, the way to obtain the key's length is by getting the GCD of the distances between each [n-gram's](https://en.wikipedia.org/wiki/N-gram) repetitions, for each respective length *n*. You can read more about it over [here](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Kasiski.html) if you're interested.



---
### References
- **Introduction to Modern Cryptography** (*Jonathan Katz and Yehuda Lindell, 2007)*