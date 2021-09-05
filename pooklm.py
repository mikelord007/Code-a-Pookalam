def beside(a, b, x1=-40, x2=40):
    a1 = a | translate(x=x1)
    b1 = b | translate(x=x2)
    return a1 + b1


# Maveli Code :-

def face():

    fccolor = color(230, 139, 108)
    baseMouthcolr = color(48, 2, 4)
    noseColrBG = color(216, 110, 86)
    noseColrFG = color(230, 139, 108)

    """ BASIC FACE OUTLINE """
    e1 = ellipse(w=100, h=180, fill=fccolor,
                 stroke_width=0) | rotate(10) | scale(0.8)
    e2 = ellipse(w=100, h=200, fill=fccolor, stroke_width=0) | rotate(
        20) | scale(0.8) | translate(0, 20)

    mainFaceDownSide = circle(r=90, fill=fccolor, stroke_width=0, x=10, y=-30)
    mainFaceUpSide = circle(r=90, fill=fccolor, stroke_width=0, x=-3, y=10)

    faceSide = beside(e1, e2, -55, 55)
    FaceOutline = faceSide + mainFaceDownSide + mainFaceUpSide

    """ MOUTH FOR MAVELI """
    mouth = ellipse(x=15, y=-45, w=90, h=100, fill=baseMouthcolr) | rotate(20)
    teeth = circle(fill="white", r=50, stroke_width=0, x=23, y=-15) | rotate(8)
    coverMouth = circle(fill=fccolor, r=70, stroke_width=0, y=18, x=19)
    finishedMouth = (mouth+teeth+coverMouth) | rotate(3) | translate(x=-3)

    """ EYES FOR MAVELI """
    eye = ellipse(0, 0, 20, 30, stroke_width=2,
                  stroke=noseColrBG, fill="white")
    eyes = beside(eye, eye, -24, 24) | rotate(17) | translate(10, 20)
    iris = circle(0, 0, 7, fill="black")
    irises = beside(iris, iris, -23, 25) | rotate(17) | translate(11.2, 19)
    pupil = circle(0, 0, 2, fill="white", stroke_width=0)
    pupils = beside(pupil, pupil, -23, 25) | rotate(17) | translate(13, 20)
    eyes = eyes + irises + pupils

    """ EYEBROWS FOR MAVELI """
    brow1 = ellipse(0, 0, 40, 10, fill="black") | rotate(48) | translate(0, 50)
    brow2 = ellipse(0, 0, 40, 10, fill="black") | rotate(-5) | translate(0, 75)
    brows = beside(brow1, brow2, -30, 20)

    finalFace = combine([FaceOutline, finishedMouth, eyes, brows])
    return finalFace


def nose():
    noseColrBG = color(216, 110, 86)
    noseColrFG = color(230, 139, 108)

    noseBG = ellipse(0, 0, 30, 20, fill=noseColrBG,
                     stroke_width=0) | translate(4)
    noseFG = ellipse(0, 0, 30, 20, fill=noseColrFG,
                     stroke_width=0) | scale(0.9)
    nose = noseBG+noseFG | rotate(19) | translate(33, -22)

    return nose


def ears():
    fccolor = color(230, 139, 108)
    earPart1 = ellipse(w=40, h=80, fill=fccolor, stroke_width=0.3)
    earPart2 = ellipse(w=50, h=80, fill=fccolor, stroke_width=0)
    ears = beside(earPart1, earPart2, -40, -
                  30) | rotate(20) | translate(-50, -22)

    return ears


def mustache():
    mustaPart1 = ellipse(w=60, h=20, fill="black")
    mustaPart2 = ellipse(
        w=28, h=9, fill="black") | translate(-20, -10) | scale(1.4) | rotate(-38)
    mustaPart3 = ellipse(w=60, h=20, fill="black") | rotate(
        38) | translate(-10, 27)
    mustaPart4 = ellipse(w=28, h=9, fill="black") | rotate(
        78) | translate(x=13, y=53) | scale(0.9)

    mustacheSide1 = (mustaPart1 + mustaPart2) | translate(12, -50) | scale(0.7)
    mustacheSide2 = (
        mustaPart3 + mustaPart4) | rotate(4) | translate(98, -50) | scale(0.7)

    mustache = mustacheSide1 + mustacheSide2
    return mustache


def crown():
    crownBaseColr = color(252, 222, 2)
    crownTopColr = color(253, 188, 2)
    crownStroke = color(148, 79, 5)
    p1 = point(0, 0)
    p2 = point(0, 5)
    p3 = point(5, 0)

    baseDark = ellipse(h=200, w=170, fill=crownTopColr,
                       stroke_width=0) | translate(8, 80) | rotate(24)
    baseLight = ellipse(h=90, w=170, fill=crownBaseColr,
                        stroke_width=0) | translate(1, 70) | rotate(20)

    topPoint = ellipse(w=110, h=50, stroke_width=1, stroke=crownStroke,
                       fill=crownTopColr) | translate(17, 160) | rotate(30)
    tippingOval = ellipse(w=100, h=100, fill=crownTopColr,
                          stroke=crownStroke) | translate(-65, 147)
    tip = polygon([p1, p2, p3], fill=crownTopColr, stroke_width=0.2,
                  stroke=crownStroke) | rotate(-103) | scale(10) | translate(-104, 208)

    crown = tip + tippingOval + topPoint + baseDark + baseLight
    return crown


def crownBase():
    innermostClr = color(219, 114, 5)
    secondClr = color(248, 170, 22)
    thirdClr = color(248, 214, 5)

    innermostCircle = circle(r=100, fill=innermostClr, stroke_width=0)
    secondCircle = circle(r=130, fill=secondClr, stroke_width=0)
    thirdCircle = circle(r=140, fill=thirdClr, stroke="white", stroke_width=2)
    minicircles = circle(r=10, fill=thirdClr, stroke_width=0) | translate(
        140) | repeat(36, rotate(10))

    crownBase = thirdCircle + secondCircle + \
        innermostCircle + minicircles | translate(-50, 110)

    return crownBase


# Pookalam Code :-

def pookalamBG():
    clr = "#0040ff"
    flowerbgClr = "#f8eb6c"
    petalClr = "#b3b300"
    bg = rectangle(w=310, h=310, fill=flowerbgClr)

    # surrounding flowers
    e1 = ellipse(h=20, w=8, stroke_width=0.3, stroke="#e91e63",
                 fill="#a977ca",) | rotate(10)
    e2 = ellipse(h=18, w=8, stroke_width=0.3, stroke="#e91e63",
                 fill="#d493ff") | rotate(-12) | translate(3, -1)
    c1 = circle(r=7, fill="#FFFF00", stroke_width=0) | translate(1.5, 7)
    surroundingFlowers = (
        c1 + e1 + e2) | scale(1.8) | rotate(-90) | translate(100) | repeat(33, rotate(11))

    # flower circles
    flowerPetal = ellipse(w=23, h=9, fill=petalClr,
                          stroke_width=0.6) | rotate(40) | translate(24)
    petals = flowerPetal | repeat(20, rotate(20))
    flowerBase = circle(r=16, fill="pink", stroke_width=1, stroke="#e414c1")
    flower = petals + flowerBase
    flowers = flower | scale(0.8) | translate(75) | repeat(12, rotate(30))

    # inner radiation
    p1 = point(0, 0)
    p2 = point(66, 5)
    p3 = point(66, -5)
    radiation1 = polygon([p1, p2, p3], fill="#F97F51", stroke_width=0)
    radiation2 = polygon([p1, p2, p3], fill="red",
                         stroke_width=0) | rotate(8.5)
    radiation = radiation1+radiation2 | repeat(22, rotate(17))

    # ring for inner radiation
    innrC = circle(r=40, fill="red", stroke_width=0.7,
                   stroke="orange") | translate(2)
    radRing = innrC

    # little tags over main flowers
    p4 = point(0, 40)
    p5 = point(30, 0)
    p6 = point(-30, 0)

    tag = polygon([p4, p5, p6], fill="#7740ca", stroke_width=0,) | repeat(
        9, rotate(40)) | scale(0.3) | translate(93, 20)
    tagCircle = tag | repeat(12, rotate(30.3))

    # sheets of paper on which pookalam lays
    sheet = rectangle(w=30, h=30, fill="orange", stroke_width=0) | rotate(
        45) | translate(120) | rotate(3)
    sheetCircle = sheet | repeat(33, rotate(11))

    sheet2 = rectangle(w=30, h=30, fill="#df6802", stroke_width=0) | rotate(
        45) | translate(130) | rotate(3)
    sheet2Circle = sheet2 | repeat(33, rotate(11))

    pookalamBG = bg + sheet2Circle + sheetCircle + radiation + \
        radRing + surroundingFlowers + flowers + tagCircle
    return pookalamBG | scale(1.2)


maveli = (crownBase() + ears() + crown() + face() +
          mustache() + nose()) | scale(0.35) | translate(15, -15)

show(pookalamBG(), maveli)
