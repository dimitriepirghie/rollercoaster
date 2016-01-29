import maya.cmds as mc
import math
from random import uniform as rand

sunSize = 10.0
sunSpeed = 3.0
planetNum = 9
frames = 200
mc.playbackOptions(loop = "continuous", min = 0, max = frames)
spinEx = "rotateY = time*10.0;"

planetSize = [0.2, 0.4, 0.5, 0.3, 2.5, 2.0, 1.5, 1.5, 0.4]

planetName = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "L573"]

cometOrbit = "translateX = 2;" + "translateY = (3 * cos(frame/5) ) + 16;" + "translateZ = (-1 * sin(frame/5) * 3) - 10;"


def createComet():
    nEmitter2 = mc.emitter (pos = (45, 0, 45), type = "direction", name = "asteroid field", r = 30)
    mc.expression(object = nEmitter2[0], string = cometOrbit, name = "CometOrbitExpression")

    nPart2 = mc.particle(name = "comet")
    mc.setAttr(nPart2[0] + ".particleRenderType", 4)
    mc.addAttr(nPart2[1], ln = "rgbPP", dt = "vectorArray")
    ramp1 = mc.arrayMapper(target = nPart2[1], destAttr = "rgbPP", inputV = "ageNormalized", type = "ramp")

    mc.setAttr("ramp1.colorEntryList[0].position", 0.0)
    mc.setAttr("ramp1.colorEntryList[0].colorR", 1.0)
    mc.setAttr("ramp1.colorEntryList[0].colorG", 0.0)
    mc.setAttr("ramp1.colorEntryList[0].colorB", 0.0)

    mc.setAttr("ramp1.colorEntryList[1].position", 1.0)
    mc.setAttr("ramp1.colorEntryList[1].colorR", 0.0)
    mc.setAttr("ramp1.colorEntryList[1].colorG", 0.0)
    mc.setAttr("ramp1.colorEntryList[1].colorB", 1.0)

    mc.connectDynamic(nPart2[0], em = nEmitter2[0])

#mc.displayRGBColor( 'background', 0, 0, 0 )

createComet()
