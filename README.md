🍉 Fruit Ninja‑Style Hand‑Tracking Game
A gesture‑controlled slicing game built with Python, OpenCV, MediaPipe Tasks, and Pygame.
Use your real hand to slice fruits on screen — no mouse or keyboard needed.
-------------------------------------------------------------------------------------------------------
🎮 Gameplay
Fruits launch into the air with physics‑based motion

Move your index finger in front of the webcam to slice them

A glowing blade trail follows your hand

Score increases for each sliced fruit

Smooth animations, real PNG fruit images, and a clean UI
_______________________________________________________________________________________________________________-

✋ Hand Tracking
This project uses the MediaPipe Tasks API (HandLandmarker) to detect the index fingertip in real time.

HandTracker class handles:

Webcam capture

Frame preprocessing

Hand landmark detection

Fingertip coordinate extraction

Integration with the game loop

Works on Python 3.10+.
_______________________________________________________________________________________________________________

🧩 Features
Realistic fruit physics (gravity, rotation, velocity)

Transparent PNG fruit sprites

Background image

Blade trail effect

Modular architecture

Easy to extend (bombs, combos, sliced fruit halves, sound effects)
_______________________________________________________________________________________________________________
# Directory Structure

fruit_ninja/
│
├── main.py
│
├── game/
│   ├── __init__.py
│   ├── fruit.py
│   ├── blade.py
│   ├── game_loop.py
│   └── utils.py
│
├── assets/
│   ├── images/
│   │   ├── apple.png
│   │   ├── banana.png
│   │   └── bomb.png
│   └── sounds/
│       ├── slice.wav
│       └── pop.wav
│
├── camera/
│   ├── __init__.py
│   ├── hand_tracking.py
│   └── camera_feed.py
│
├── requirements.txt
└── README.md
_______________________________________________________________________________________________________________

🚀 Future Improvements
Fruit splitting animation

Bombs + game over screen

Sound effects

Combo system

Difficulty scaling

High‑score saving
