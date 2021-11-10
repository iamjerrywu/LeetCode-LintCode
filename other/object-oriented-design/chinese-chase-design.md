# Chinese Chase Design

## Problem

![](<../../.gitbook/assets/Screen Shot 2021-07-20 at 10.27.45 AM.png>)

## Procedure

### Clarify

* Each player has its score (win + 1, lose - 1, tie + 0)
* Players are red/black, and initilize randomly
* No time limitation
* How to clarify tie?
  * Sol1: If total steps exceed threshold, then it's a tie (Recommended, much easier)
  * Sol2: If both are repeating the same steps, then it's a tie
  * Sol3: If both request it's a tie, then it's a tie

### Use Case

Three status:

* Initialization&#x20;
  * Join the game
    * A player joins a game to play
  * set up the game
    * Initialize the board with all pieces placed at the right place
* Play&#x20;
  * make move
    * Determine which player should take move
    * Check if the move is valid. If yes, return true and make the move, else return false
  * change player
* Win/Lose/Tie check&#x20;
  * &#x20;Check for win
    * Check if current player wins
  * Increase steps
    * If reach max steps, then it a tie
  * Calculate points
    * If current player wins, reword current player and take one point off from other one

## Solution&#x20;

![](<../../.gitbook/assets/Screen Shot 2021-07-20 at 10.40.36 AM.png>)

###
