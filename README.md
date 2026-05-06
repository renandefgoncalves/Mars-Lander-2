# Mars Lander - Episode 2

## The Goal
The goal for your program is to safely land the "Mars Lander" shuttle, the landing ship which contains the Opportunity rover. Mars Lander is guided by a program, and right now the failure rate for landing on the NASA simulator is unacceptable.

This puzzle is the second level of the "Mars Lander" trilogy. The controls are the same as the previous level but you must now control the angle in order to succeed.

## Rules
Built as a game, the simulator puts Mars Lander on a limited zone of Mars sky.
<img width="468" height="265" alt="image" src="https://github.com/user-attachments/assets/0bf2d10a-1e3a-45d7-b7a3-2bb82e6b1b5d" /> The zone is **7000m** wide and **3000m** high.

There is a **unique area of flat ground** on the surface of Mars, which is at least **1000** meters wide.

Every second, depending on the current flight parameters (location, speed, fuel ...), the program must provide the new desired tilt angle and thrust power of Mars Lander:
<img width="505" height="208" alt="image" src="https://github.com/user-attachments/assets/be82258f-453b-4292-8190-3656e94a1760" />
- **Angle** goes from -90° to 90°.
- **Thrust power** goes from 0 to 4.

The game simulates a **free fall** without atmosphere. Gravity on Mars is **3.711 m/s²**. For a thrust power of X, a push force equivalent to **X m/s²** is generated and **X liters of fuel** are consumed. As such, a thrust power of 4 in an almost vertical position is needed to compensate for the gravity on Mars.

### Landing Requirements
For a landing to be successful, the ship must:
1. Land on **flat ground**.
2. Land in a **vertical position** (tilt angle = 0°).
3. **Vertical speed** must be limited (≤ 40m/s in absolute value).
4. **Horizontal speed** must be limited (≤ 20m/s in absolute value).

> **Note:** Tests and validators are only slightly different. A program that passes a given test will pass the corresponding validator without any problem.

## Game Input
The program must first read the initialization data from standard input. Then, within an infinite loop, the program must read the data related to Mars Lander's current state and provide the instructions to move the ship.

### Initialization Input
- **Line 1:** `surfaceN` (the number of points used to draw the surface).
- **Next `surfaceN` lines:** `landX landY` (coordinates of a ground point). The surface is formed by linking these points sequentially.
    - First point: `landX = 0`.
    - Last point: `landX = 6999`.

### Input for One Game Turn
A single line with 7 integers: `X Y hSpeed vSpeed fuel rotate power`
- **X, Y:** Coordinates of Mars Lander (meters).
- **hSpeed, vSpeed:** Horizontal and vertical speed (m/s).
- **fuel:** Remaining fuel in liters.
- **rotate:** Current rotation angle in degrees.
- **power:** Current thrust power.

### Output for One Game Turn
A single line with 2 integers: `rotate power`
- **rotate:** Desired rotation angle. (Limited to +/- 15° per turn).
- **power:** Desired thrust power (0-4). (Limited to +/- 1 per turn).

## Constraints
- 2 ≤ `surfaceN` < 30
- 0 ≤ `X` < 7000 | 0 ≤ `Y` < 3000
- -500 < `hSpeed`, `vSpeed` < 500
- 0 ≤ `fuel` ≤ 2000
- -90 ≤ `rotate` ≤ 90
- 0 ≤ `power` ≤ 4
- Response time per turn ≤ 100ms
