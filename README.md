# 03Breakout
03Breakout
# 03Breakout
03Breakout

#Breakout Game - Slow Motion Power

Implementation of the SlowMotion power that reduces the speed of all balls on screen.

## Key Features
- **Slow Motion Power**: When the power is activated with the 6th frame provided in the project, all balls reduce their speed to 50% for **5 seconds**
- **Timer System**: Implemented a timer to control the duration of the effect
- **Attribute Modifications**: Added the `speed_factor` parameter to balls to dynamically control their speed
- **Shoot power**: When the cannons are active, you can shoot fireball with the key "z" only 5 times, you cant shoot if a fireball is active in game

## Code Structure
### Modified Files
1. **SlowMotion.py**
- Definition of the created SlowMotion power

2. **ball.py**
- Added the `speed_factor` attribute to control the speed of each ball
- Modified the motion methods to apply the speed factor

3. **PlayState.py**
- Integration of the power into the power array
- Timer management and effect activation/deactivation
