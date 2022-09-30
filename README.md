# cse210-02

## objects:

### director  (handles logic/game loop) (Alex/Joshua)
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
    
### deck (Mike)
- card  (generate card value)  deck.draw_card  (int) range 1-13

### welcome  (Mark)
- start (function) method welcome.start
- ask player for name welcome.get_name (store in player.name)
- introduction/rules (print stmt) welcome.display_rules


