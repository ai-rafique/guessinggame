# guessinggame

This is the view counts guess game :)
You will be asked which 1 of the given 2 celebrities have more view count.

##main.py
This is where the magic happens. The main game loop.
You will be asked who has more followers. 
The selection for the questions is done on random.
On bad guess, you will get the number counts.
On correct guess you will WIN

##data.py
Contains a list of dictionaries with name, count, description and country.
Currently, name and count will be extracted for the game purpose.

##art.py
cotains a funky ASCII art 


## How the randomiser works
If you look at data.py, you will see that the follower_count is arranged in descending order.
Although it is random, even if you do not set the seed, I saw in my observation that the
first value extracted is smaller than the second. Meaning option B will likely be the answer
as compared to option A. Although the numbers are quite near.
Here is an example.
I used a compare function on random values from the dictionary on value of randomly selected counts.

In 1000 iterations, the values are compared.
This was done 10 times.
The probability of Option B being bigger was 90%.
The probability within the 1000 run each was somewhat 47 53 for A and B respectively.

To mitigate this, I have halved the list into even and odd and then used the choice function.
This actually made things worse. In 10 tries, I got option B 10/10. On the 11th, i got A. 
In 15 tries, 2 A. In 20 tries 3. In 30 tried 3.

Then, my dumbass realized I could just shuffle the damn list and then do serious stuff with it.
When I did it with the normal arrangment I got 1 A and 9B in 10 tries.
When I did that with the even odd arangement, I got a 5A 5B out of 10 tries.

So that is how my randomiser works, the list is shuffled and then option A is all odd , option B is all even

## FUTURE WORK
1) Smarter random picking
