**DanceBox: Move to Win!** is an interactive game built using Python and OpenCV, where players must use their body to match a series of on-screen targets. Inspired by dance games like *Just Dance*, this game challenges you to move different parts of your body into green target zones that appear randomly on the screen. The faster you react, the more points you earn!

### **How to Play**

1. **Start the Game**: Launch the game, and the camera will start capturing your movements.
2. **Move Your Body**: The game will show random target areas (like the head, arms, or torso) in green boxes.
3. **Match the Target**: Move the relevant body part into the green box. If any body part (head, arm, leg, or torso) crosses into the box, you earn points.
4. **Points**: The game awards points for each successful move, and the boxes appear more frequently as you play!
5. **Keep Moving**: Boxes disappear after a short time, and new ones randomly appear. React quickly to keep scoring high!

### **Features**
- **Randomized Target Boxes**: Green boxes will appear on various parts of the screen at random locations.
- **Body Part Detection**: The game detects your head, arms, torso, and legs to ensure you are in the right position.
- **Frequent Challenges**: The boxes spawn faster as you play, increasing the difficulty and making the game more fun.
- **Real-time Scoring**: The more you move into the target boxes, the higher your score becomes!

### **Requirements**

To run the game, you need to install the following libraries:

- **Python 3.x**: Make sure you have Python installed on your machine.
- **OpenCV**: For webcam capture and image processing.
- **MediaPipe**: For detecting body landmarks.
- **Pygame**: For displaying the score and game text.

You can install the necessary libraries with the following commands:

```bash
pip install opencv-python mediapipe pygame
```

### **Installation and Running the Game**

1. **Clone this repository** (or download the game script).
2. Install the required dependencies (listed above).
3. **Run the game** by executing the Python script.

```bash
python main.py
```

Make sure your webcam is enabled, as the game uses it to detect your body movements.

### **Controls**

- **Use your body to move parts (head, arms, legs, torso)** into the green target boxes.
- The game detects body parts using the webcam, so make sure you’re in front of the camera.
- **Press 'Q' to exit** the game at any time.

### **Gameplay Example**

The game will show a message like:  
*“Move your LEFT ARM to the green box!”*

You need to raise or position your left arm in the green box area to earn points. If successful, you'll get a message like:  
*"Good Job! +10 Points!"*

The boxes will disappear after a short time, and new target boxes will appear in different locations.

### **Customizing the Game**

- **Increase the difficulty**: You can adjust the spawn rate of the target boxes by modifying the time delay (`0.5` seconds) between each box's appearance.
- **Adjust body part detection**: The game uses MediaPipe's pose estimation to detect key landmarks like shoulders, hips, elbows, and knees.

Feel free to modify the code to add new features, change the target regions, or make the game even more fun!

---

Enjoy playing **DanceBox: Move to Win!** and show off your dance moves! 🚶‍♂️💃🕺

---
Readme made with the assistance of AI
