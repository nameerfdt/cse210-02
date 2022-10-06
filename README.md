# HiLo

Play Hilo starting with 300 point and see how many more points you can earn before dropping to 0! 
If you're correct, you'll earn 100 points. If you're wrong, you'll lose 75 points.
Drop to 0 points and the game ends or you can decide to keep playing or not. 

## Getting Started
___

Make sure you have Python 3.10 or newer installed and running on your machine. Open a terminal and 
browse to the project's root folder. Start the program by running the following command.
```
<ENTER COMMAND TO START PLAYING>
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure


### director  (handles logic/game loop) (Joshua)
- call welcome.start
- compare_card (method) director.compare
- update_total (int) director.update
- current card (int) director.current_card
- previous card (int) director.prevous_card
- display card (method - how print out to user)  director.display_card
- game over/continue (check if below 0, if is not ask if player wants to continue) - director.game
    
### player (Tracy)
- name  player.name (str)  
- current score - always start at 300  player.score (int) +=
- guess - high/lo (str) player.guess  h/l 
    - Write in code for upper/lower h/l for input
    
### deck (Alex)
- card  (generate card value)  deck.draw_card  (int) range 1-13

### welcome  (Mark)
- start (function) method welcome.start
- ask player for name welcome.get_name (store in player.name)
- introduction/rules (print stmt) welcome.display_rules

## Required Technologies
---
* Python 3.10

## Authors
---
* Alex Dahl (alexdahl@byui.edu)
* Tracy Freeman (nameerfdt@byui.edu)
* Joshua Herman (EMAIL)
* Mark Perry (per19039@byui.edu)

