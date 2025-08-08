Welcome to the ReadMe for Nutmeg's Asteroids Game

You'll need up, down, left, right arrow keys to play this game rather than using a, d, w, s. The spacebar is for shooting at asteroids. 











Learning Notes (abbrev. LN with file location)

If my code were handwritten out (as I often do with the lessons in Boot.Dev) these are some of the notes I'd be making in the margins to talk to myself about what's going on. Granted, I may have abused copy and paste a little while using a digital format, but Boot's reponses are often in lieu of a textbook. It is what it is. These may or may not be helpful to others. They're here for me. 

LN 1 player.py line 7: This really confused me but Boots explained it as CircleShape needs to know where (x,y) and what size, radius. For the subclass Player, what size will aways be the same but where can change. So when we initialze Player all it expects is x and y. We use the super().__init__(x,y, PLAYER_RADIUS) to help bridge the gap between Player and CircleShape by telling CircleShape that radius is constant (and what that radius is). (Where the constant is in the "from constants import *" bit).

LN 2 asteroid.py line 6: I needed the parent constructor specifically because it calls the hidden self.position and self.velocity variables that I needed for asteroid creation. In declairing my own constructor, I was able to modify the expected input for Asteroids.

LN 3 main.py line 31: This line isn't necessary but here's the summary of a conversation I had with Boots:"Haha, my apprentice, you've stumbled upon one of the ancient mysteries of programming! Indeed, many a line of code has found its way into a program, seemingly by magic, just to make an error disappear, only to reveal its true, often peculiar, purpose later on!

You've hit on a very keen observation about why that line might have seemed necessary. When you first wrote your collision detection, if you tried to write something like:

if shot.collision_happens(asteroid):
    # ...

...and shot hadn't been created or defined before this line in that particular scope, Python would rightly say, "Whoa there, what's shot? I don't know what that variable is!" That's the NameError or UnboundLocalError you likely encountered.

Your solution to define shot = Shot(player.position.x,player.position.y) at the top of main() was a clever way to satisfy Python's need for shot to exist so that line of code could run. It did define shot, and the error went away! The catch, as you brilliantly discovered, was that this shot was just a single, stationary bullet.

The correct way, as we explored, is that your player.shoot() method dynamically creates new Shot objects and adds them to the shots pygame.sprite.Group(). Then, your collision loop for shot in shots: iterates over all the Shot objects currently in that shots group, ensuring that every active bullet is checked for collisions.

So, the "mystery line" was a temporary fix that helped you bypass a definition error, but the true solution lay in understanding how and when Shot objects are created and managed within the game's dynamic flow. You learned a very valuable lesson through that process!"

LN 4 asteroid.py line 31: So I though split_spawn1.velocity = self.velocity would assign the vector values associated with self.velocity to my split_spawn1 velocity. Not so. Boots said think of there being a piece of paper that has the wanted info on it. self.velocity and split_spawn1 both point to the same peice of paper so to speak. I need to use the copy method on self.velocity to create a "new piece of paper" to work with and manipulate. Also it didn't seem to be creating two new asteroids on two different trajectories. Just the same asteroid smaller. Boots thought it was two smaller asteroids superimposed without new vector information. Here is his summary of our debugging process to fix the issue:

The Debugging Journey
1. Initial Problem Identification

    Symptom: Only one stationary asteroid appeared instead of two moving asteroids
    Your approach: You clearly described what you expected vs. what you observed

2. Code Review & Hypothesis Formation

    My analysis: Suspected velocity assignment and rotation issues
    Key questions: Are velocities being set? Are rotations working?

3. First Debugging Attempt - Print Statements

    Added: Print statements to see original velocity vs. new velocities
    Discovery: All velocities were identical - rotation wasn't working at all

4. Deeper Investigation - Method Behavior

    Hypothesis: Maybe rotate() returns a new vector instead of modifying in-place
    Test: Added more granular prints around the rotation call

5. Root Cause Analysis - Object References

    Discovery: You were assigning the same vector object to multiple asteroids
    Solution: Introduced .copy() method to create separate vector objects

6. Method Return Value Investigation

    Issue: rotate() still wasn't working even with .copy()
    Hypothesis: rotate() might return a new vector rather than modify existing
    Solution: Assign the return value: self.velocity.copy().rotate(angle)

7. Mysterious Resolution

    Outcome: Suddenly started working (possibly due to a subtle change during debugging)
    Your wisdom: Clean up debug code and test again

8. Final Verification

    Confirmed: Splitting works correctly
    Added: Final requirement (1.2x velocity scaling)

Key Debugging Principles We Used:

    Isolate the problem - Focus on one issue at a time
    Make the invisible visible - Use print statements to see what's happening
    Test assumptions - Don't assume methods work the way you think they do
    Understand object behavior - References vs. copies, return values vs. in-place modifications
    Clean up and verify - Remove debug code and ensure it still works
