import cv2
import numpy as np

# Parâmetros intrínsecos
focal_length = 1000  # Exemplo, ajuste conforme sua câmera
principal_point = (320, 240)  # Exemplo, ajuste conforme sua câmera

K = np.array([[focal_length, 0, principal_point[0]],
              [0, focal_length, principal_point[1]],
              [0, 0, 1]])

# Parâmetros extrínsecos (exemplo)
R = np.eye(3)  # Matriz de rotação de identidade
t = np.array([0, 0, 0])  # Vetor de translação

# Ponto na câmera
u = 0
v = 0
w = 1.0

# Ponto no sistema de coordenadas da câmera
camera_point = np.array([u * w, v * w, w])

# Inversa da projeção perspectiva
inv_K = np.linalg.inv(K)
inv_camera_point = np.dot(inv_K, camera_point)

# # Inversa da transformação do ponto da câmera para o mundo
# inv_R = np.linalg.inv(R)
# inv_t = -t
# world_point = np.dot(inv_R, inv_camera_point[:-1]) + inv_t

# Inversa da transformação do ponto da câmera para o mundo
inv_R = np.linalg.inv(R)
inv_t = -t
world_point = np.dot(inv_R, inv_camera_point) + inv_t

print("Ponto no mundo:", world_point)