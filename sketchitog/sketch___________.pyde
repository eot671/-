x1=0
y1=0
x2=0
y2=0
up=0
speedx=10
gran=350 #границы экрана
storona=100 #сторна блока
gamestart=True
xrect=0
yrect=0
speedyrect=10
rectdown=False
blocks=[]
lose=False #блок промахивается по башне
score=0
class Block:
    def __init__(self,xblock,yblock):
        self.x=xblock
        self.y=yblock
def setup():

    global x1,y1,x2,y2,bg
    bg=loadImage("town.png")
    size(1000,1000)
    x1=width//2
    y1=0
    x2=width//2
    y2=250
def draw():
    global x2,y2,speedx,gran,storona,xrect,yrect,speedyrect,gamestart,rectdown,Block,blocks,up,lose,score,bg
    image(bg,0,0,width,height)
    textSize(35)
    text(score,3*width//4,30)
    if rectdown==True or gamestart==True:
        for i in range(len(blocks)):
            rect(blocks[i].x,up+blocks[i].y,storona,storona)
            if yrect>blocks[i].y+up:
                gamestart=False
                rectdown=False
                lose=True
    if lose==True:
        textSize(70)
        text("Lose:(",450,500)   
            
    if gamestart==True:
        x2=x2+speedx
        if x2>width-gran:
            speedx=-1*speedx
        if x2<gran:
            speedx=-1*speedx
        line(x1,y1,x2,y2)
        xrect=x2-storona/2
        yrect=y2
        fill(255,136,0)
        strokeWeight(4)
        rect(xrect,yrect,storona,storona)
    if rectdown==True:
        x2=x2+speedx
        speedyrect=5
        if x2>width-gran:
            speedx=-1*speedx
        if x2<gran:
            speedx=-1*speedx
        line(x1,y1,x2,y2)
        yrect=yrect+speedyrect
        rect(xrect,yrect,storona,storona)
        for i in range(len(blocks)):
            if yrect>blocks[i].y-storona+up and xrect+0.5*storona>blocks[i].x and xrect<0.5*storona+blocks[i].x:
                speedyrect=0
                gamestart=True
                rectdown=False
                blocks.append(Block(xrect,yrect-up))
                score=score+1
        if yrect>height-storona :
            speedyrect=0
            rectdown=False
            gamestart=True
            blocks.append(Block(xrect,yrect-up))
        if len(blocks)>5:
            blocks.pop(0)
            up=up+0.96*storona

        
def keyReleased():
    global rectdown,gamestart
    if key == ' ':
        rectdown=True
        gamestart=False
        
