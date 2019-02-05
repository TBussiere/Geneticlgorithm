import pybullet as p
import numpy as np
import time
# import Shape as s
import util


# créé la fenetre de base
p.connect(p.GUI)
# Defini le nombre d'objet pour la "RandomShape"
nbobj = 5
# defini un radius de base
rad = 0.05
# defini une mass de base
mass = 1
# defini une rotation de base
rotation = [0, 0, 0, 1]
# defini une position de base
pos1 = [0, 0, 2]
basex = pos1[0]
basey = pos1[1]
basez = pos1[2]

shape = util.initSim(nbobj, rad, pos1)

p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

maxFit = 0

# Le "run"
while (1):
    rkey = ord('r')
    keys = p.getKeyboardEvents()
    if rkey in keys and keys[rkey] & p.KEY_WAS_TRIGGERED:
        p.resetSimulation()
        shape = util.initSim(nbobj, rad, pos1)
        maxFit = 0
        continue

    posbody = p.getBasePositionAndOrientation(shape)[0]
    curCam = p.getDebugVisualizerCamera()
    p.resetDebugVisualizerCamera(
        cameraDistance=curCam[10], cameraYaw=curCam[8],
        cameraPitch=curCam[9],
        cameraTargetPosition=posbody)

    curx = posbody[0]
    cury = posbody[1]
    curz = posbody[2]

    fitness = (np.abs(curx-basex) + np.abs(cury-basey))

    if maxFit < fitness:
        maxFit = fitness
        print(maxFit)

    time.sleep(1/65)


p.disconnect()
