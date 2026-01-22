# ASCII Animation Player Using Python

## Project Overview
The ASCII Animation Player is a simple animation system developed using Python. 
It displays frame-based animations in the terminal using ASCII characters. 
The system automatically switches between different animation states such as idle, walk, and run.

This project was developed following the Software Development Life Cycle (SDLC).



## 1. Requirement Analysis

The goal of this project is to design and implement a simple animation player that demonstrates animation logic without using external libraries.

### Functional Requirements
- The system shall load animation frames from text files
- The system shall display animations continuously
- The system shall support multiple animation states (idle, walk, run)
- The system shall automatically switch between animations

### Non-Functional Requirements
- The system shall be implemented using standard Python
- The system shall be easy to understand and maintain
- The animation playback shall be smooth and readable in the terminal



## 2. System Design

The system is divided into modular components to improve maintainability.

### Modules
- **AnimationLoader**: Loads animation frames from text files
- **AnimationPlayer**: Controls animation playback and timing
- **Main Application**: Manages animation switching and program execution

### Project Structure
ascii_animation_player
  main.py
  animation_loader.py
  animations/
    idle.txt
    walk.txt
    run.txt


## 3. Implementation

The project was implemented using Python.

- `animation_loader.py` reads animation frames from `.txt` files
- `animation_player.py` handles frame display and timing
- `main.py` controls animation switching and application flow

The implementation strictly follows the system design to ensure consistency between design and code.

## 4. Testing

The system was tested by:
- Confirming that animation files load correctly
- Verifying smooth animation playback
- Testing automatic animation switching
- Ensuring the application exits correctly using Ctrl + C


## 5. Deployment

The project was deployed by pushing the source code to a GitHub repository.


## 6. Maintenance

- Updating animation frame files to improve or change animations
- Adding new animation states such as jump or attack
- Adjusting animation speed for better visual output
- Fixing bugs or errors discovered during use
- Refactoring code to improve readability and maintainability


## How to Run the Project

1. Ensure Python is installed
2. Open the project folder in a terminal
3. Run the command:
  python main.py

  I use Visual code studio so pressing run with on without debugging works
