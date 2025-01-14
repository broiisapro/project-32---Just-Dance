import cv2
import mediapipe as mp
import time
import random
import pygame

# Initialize Pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Just Dance')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont("Arial", 30)

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

score = 0
key_pressed = False
dance_moves = ['RAISE_LEFT_ARM', 'RAISE_RIGHT_ARM', 'MOVE_LEFT', 'MOVE_RIGHT']

# Target regions for body parts
target_region = {
    'head': (100, 100, 150, 150),
    'left_arm': (50, 200, 150, 250),
    'right_arm': (400, 200, 500, 250),
    'left_leg': (50, 400, 150, 450),
    'right_leg': (400, 400, 500, 450),
    'torso': (250, 200, 350, 300)
}

# Function to check if the body part is within the target region
def is_part_in_region(part_coords, region):
    x, y = part_coords
    x1, y1, x2, y2 = region
    return x1 < x < x2 and y1 < y < y2

# Function to get the player's center
def get_player_center(landmarks):
    try:
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
        center_x = (left_hip.x + right_hip.x) / 2
        center_y = (left_hip.y + right_hip.y) / 2
        return (center_x, center_y)
    except:
        return None

# Function to calculate angle between three points
def calculate_angle(p1, p2, p3):
    angle = abs((p2[1] - p1[1]) * (p3[0] - p1[0]) - (p2[0] - p1[0]) * (p3[1] - p1[1]))
    return angle

# Function to check if a dance move is correct
def check_move(move, landmarks):
    if move == 'RAISE_LEFT_ARM':
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value]
        if left_elbow.y < left_shoulder.y:  
            # Check if the left arm is raised
            return True
    elif move == 'RAISE_RIGHT_ARM':
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        if right_elbow.y < right_shoulder.y:  
            # Check if the right arm is raised
            return True
    elif move == 'MOVE_LEFT':
        left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
        if left_hip.x < 0.4:  
            # Check if the player is moving left
            return True
    elif move == 'MOVE_RIGHT':
        right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
        if right_hip.x > 0.6:  
            # Check if the player is moving right
            return True
    return False

# Main game loop
def game_loop():
    global score, key_pressed

    last_move_time = time.time()
    move = random.choice(dance_moves)
    move_time = random.randint(3, 5)
    target_region_name = random.choice(list(target_region.keys()))
    target_box = target_region[target_region_name]

    target_box_visible = True
    last_box_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        results = pose.process(frame)

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            # Draw landmarks on the screen
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            player_center = get_player_center(landmarks)

            # Check if the player performed the correct move
            if check_move(move, landmarks):
                score += 10
                key_pressed = True
                move = random.choice(dance_moves)
                last_move_time = time.time()
                target_region_name = random.choice(list(target_region.keys()))
                target_box = target_region[target_region_name]
                target_box_visible = True

            # Check if the body part is within the target box
            for landmark_id, landmark in enumerate(landmarks):
                part_coords = (landmark.x * frame.shape[1], landmark.y * frame.shape[0])

                if is_part_in_region(part_coords, target_box) and target_box_visible:
                    # Award points
                    score += 10
                    cv2.putText(frame, "Good Job! Points Awarded", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    target_box_visible = False
                    last_box_time = time.time()

            # Display the green box
            if target_box_visible:
                x1, y1, x2, y2 = target_box
                cv2.rectangle(frame, (x1, y1), (x2, y2), GREEN, 2)

        # Display the current move and score
        move_text = font.render(f"Move: {move}", True, BLACK)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.fill(WHITE)
        screen.blit(move_text, (screen_width // 3, screen_height // 4))
        screen.blit(score_text, (screen_width // 3, screen_height // 2))
        pygame.display.update()

        # Show the frame from the webcam in new window
        cv2.imshow('Dance Game', frame)

        if not target_box_visible and time.time() - last_box_time > 0.5:

            new_target_box = None
            while new_target_box is None or is_part_in_region((player_center[0] * frame.shape[1], player_center[1] * frame.shape[0]), new_target_box):
                target_region_name = random.choice(list(target_region.keys()))
                new_target_box = target_region[target_region_name]
            
            target_box = new_target_box
            target_box_visible = True

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release camera
    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

# Run the game
game_loop()