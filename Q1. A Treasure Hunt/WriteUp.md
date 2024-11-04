# A Treasure Hunt (Write-Up)
This question is rather simple, just follow the hints and enter the correct path in the URL <br>

P.S. If you want to host this yourself it uses fastAPI, and make sure to run it in dev mode as /docs wont work otherwise

## The Hints and Paths
<b>Note: if you see curly brackets {}, that means you can fill it with whatever you want</b> <br> 

Home/Root: <br>
Here it's easy, just go to "/magic-number" as it says <br>

Hint 1: "Did you know I have unicorns, each one has an ID so I can keep track of it, you should check them out." <br>
Explanation: Here Im talking about unicorns and how each one has an ID so you have to go to "/unicorns/{anythin in here}" <br>

Hint 2: "Oh no, a goblin stole one of them, he says he needs food in order to give it back." <br>
Explanation: Here you gotta feed the goblin somehow, so you have to "/goblin/{anything in here}" <br>

Hint 3: "The unicorn is safe now, but the goblin jumped in a weird portal, could it go to a universe parallel to ours?" <br>
Explanation: I was being hyper specific here, so it's obviously "/parallel-universe" (Hi Gnavin :D) <br>

Hint 4: "okay yeah, this is definetly a parallel universe, what year are we in right now?." <br>
Explanation: Tell them the time go to "/year/{any number}" <br>

Hint 5: "okay enough moving around time and space, Im hungry, I could go for some food, maybe a taco." <br>
Explanation: Hyper specific again (and hungry), go to "/taco" <br>

Hint 6: "dang it a cat stole my taco." <br>
Explanation: Darn cat, chase it, go to "/cat" <br>

Hint 7: "running after the cat ended up hurting me, I stepped on a banana peel, I dont think I need to explain what happened." <br>
Explanation: This one isn't so obvious, but if you've seen tom and jerry you know they "/slip" on the banana peels <br>

Hint 8: "congrats, the flag is in /flag" <br>
Explanation: This one is a trick, going to "/flag" will only make you wait 5 minutes and not result in anythin, the real answer is hidden in the "injury_level" part, if you look closley you can see the word "DOCS" in full caps, that only means one thing, go to "/docs" and you'll find the flag there <br>

And congrats, you're done :D <br>