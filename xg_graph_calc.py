import matplotlib.pyplot as plt
import mplsoccer
from mplsoccer import Pitch, VerticalPitch
import numpy as np
import random
import math

def calculate_xg(distance, angle):
  """
  distance - distance of the shot (in meters)
  angle - angle of the shot (in degrees)
  """
  prob_angle = 1/(1+math.exp(3.71 - 3.45*angle))
  prob_dist = 1/(1+math.exp(-0.52 + 0.17*distance))
  return prob_angle*prob_dist

def model_pitch():
  pitch = VerticalPitch(pitch_color='grass', line_color='white', stripe=True, half=True, axis=True, label=True, tick=True)
  fig, ax = pitch.draw()

def add_actors(ball_x, ball_y):
  #plot player and ball in random area in the attacking third
  #plt.plot(40, 100, 'bo', markersize=10)
  #plt.plot(40, 102, 'wo', markersize=5)
  #player_rand_x = random.uniform(15.0, 65.0)
  #player_rand_y = random.uniform(95.0, 115.0)
  plt.plot(ball_x, ball_y-2, 'bo', markersize=10)
  plt.plot(ball_x, ball_y, 'wo', markersize=5)

  #ball_x = player_rand_x
  #ball_y = player_rand_y+2
  #plt.plot(ball_x, ball_y, 'ro', markersize=10)

  #plot goalkeeper in random area of six-yard box
  #plt.plot(40, 116, 'rx', markersize=10)
  #plt.plot(random.uniform(35.0, 45.0), random.uniform(115.0, 120.0), 'rx', markersize=10)

  #plot defender(s) in random area of eighteen-yard box
  #plt.plot(46, 108, 'ro', markersize=10)
  #plt.plot(random.uniform(20.0, 60.0), random.uniform(105.0, 115.0), 'ro', markersize=10)

def get_distance_and_angle(x, y):
    # Define goal center and endpoints
    center_of_goal = np.array([40.0, 120.0])
    left_of_goal = np.array([30.0, 120.0])
    right_of_goal = np.array([50.0, 120.0])
    ball_position = np.array([x, y+2])

    # Compute distance from ball to center of goal
    distance = np.linalg.norm(center_of_goal - ball_position)

    # Compute vectors from ball to goal endpoints
    vector_left = left_of_goal - ball_position  # Vector to the left goal post
    vector_right = right_of_goal - ball_position  # Vector to the right goal post

    # Compute dot product and norms
    dot_product = np.dot(vector_left, vector_right)
    norm_left = np.linalg.norm(vector_left)
    norm_right = np.linalg.norm(vector_right)

    # Compute angle in radians using arccos
    angle_radians = np.arccos(dot_product / (norm_left * norm_right))

    # Convert to degrees
    angle_degrees = np.degrees(angle_radians)

    return distance, angle_degrees


ball_x = random.uniform(15.0, 65.0)
ball_y = random.uniform(95.0, 115.0)

model_pitch()
add_actors(ball_x, ball_y)
distance, angle = get_distance_and_angle(ball_x, ball_y)
#print("Distance: " + str(distance))
#print("Angle: " + str(angle))
#print("Ball X: " + str(ball_x))
#print("Ball Y: " + str(ball_y))

calculated_xg = calculate_xg(distance, angle)
print("Expected Goal Value: " + str(calculated_xg))