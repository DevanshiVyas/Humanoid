#Name:Devanshi Vyas
#ID no.201101141
#This program constructs a humanoid
#Separate modules construct the various body parts namely torso,head,
#left and right, upper and lower arms and legs.
#Hierarchical modelling,as explained in the class, is used.
# All of these can be individually moved using various keys( Please see the keyboard 
#function for more details) .It also does the Rajesh khanna signature step by shaking both
#hands,waves a hi and also does random dancing.

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception

#statement for import

import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Initializing Humanoid body parts
#initialise the value of the radius of the cylinder for creating the robot's torso
Torso_r=0.1
#initialise the value of the height of the cylinder for creating the robot's torso
Torso_ht=0.4 

#initialise the value of the height of the cube for creating the robot's upper arm
U_arm_h=0.25

#initialise the value of the width of the cube for creating the robot's upper arm
U_arm_w=0.03

#initialise the value of the height of the cube for creating the robot's lower arm
L_arm_h=0.25
#initialise the value of the width of the cube for creating the robot's lower arm
L_arm_w=0.05

#initialise the value of the leg/hip width for creating the robot's legs
leg_w = 0.2

#initialise the value of the height of the cube for creating the robot's upper leg
U_leg_h=0.35
#initialise the value of the width of the cube for creating the robot's upper leg
U_leg_w=0.08

#initialise the value of the height of the cube for creating the robot's lower leg
L_leg_h=0.3
#initialise the value of the width of the cube for creating the robot's lower leg
L_leg_w=0.06



#Setting X-axis & Y-axis positions of head.
head_x=0.1
head_y=Torso_ht
#Setting X-axis & Y-axis positions of left and right upper and lower arms.
Left_U_arm_X= - Torso_r
Right_U_arm_X = Torso_r
Left_U_arm_Y=Right_U_arm_Y=Torso_ht
Left_L_arm_Y=Right_L_arm_Y=L_arm_h

#Setting X-axis & Y-axis positions of left and right upper and lower legs.
Left_U_Leg_X=-1.0 * leg_w / 2
Right_U_Leg_X=leg_w / 2
Left_U_Leg_Y=Right_U_Leg_Y=-0.08
Left_Lower_Leg_Y=Right_L_Leg_Y=L_leg_h
#Setting initial values for viewing and rotation parameters
angle = 0
t0=0.0
t1=0.0
t2=0.0
t3=90.0
t4=0.0
t5=90.0
t6=0.0
t7=180.0
t8=0.0
t9=180.0
t10=0.0
x1=2
y1=2
z1=2
x2,z2=0,0
y2=1
seconds=0.0

# Declare arrays for controlling the moves namely shaking hands, random dance and stop
# respective moves for shaking hands, stop, dance are (0,1,2)
# arm_rot for left and right arm rotation
# tpar is an array of parameters tpar[0] and tpar[1] for direction and distance
arm_rot=[0.0,0.0]  
tpar=[0.0,0.0]  
move=[0,0,0,1]
#roangle arrays are necessary for manipulation of the rotation parameters
#t0 to t10 especially in idle module which makes it possible for the 
#various moves to be executed
roangle_min=[-30.0,-5.0,0.0,0.0,-10.0,0.0,-10.0,160.0,0.0,200.0,0.0,0.0]
roangle_max=[30.0,15.0,0.0,-90.0,-35.0,90.0,-35.0,200.0,0.0,160.0,0.0,0.0]
roangle_freq=[0.5,3.0,0.0,3.0,2.0,3.0,2.0,3.0,0.0,3.0,0.0,0.0]

#module/function for setting the view
def changeView(eyex,eyey,eyez,upX,upY,upZ):
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upX, upY, upZ)


# the primary display function
def display():
  global angle


  #clear buffers to preset values
  #Masks to be cleared.
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  #specify which matrix is the current matrix. Currently MODELVIEW Matrix selected.
  #Used in relation to view and camera.
  glMatrixMode(GL_MODELVIEW)
  
  #TORSO
  #replace the current matrix with the identity matrix.Identity matrix resets
  #projection/model view matrix to its default state.
  glLoadIdentity()

  #define a viewing transformation
  
  gluLookAt (0.0, 2.0, 6.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0)
  changeView(x1,y1,z1,x2,y2,z2)
  glTranslatef(0,0,angle)
  
	#For proper positioning of the bot
  glTranslatef(tpar[1], -2.0, 0.0)
   #Variables for dance rotations/turns
  rot_x=0.0
  rot_y=0.0
  # For setting the direction faced by bot
  glRotatef(tpar[0], 0.0, 1.0, 0.0) 
  
  #Torso
  #t0 Specifies the angle of rotation.
  glRotatef(t0, 0.0, 1.0, 0.0)
  green()
  torso()
  glPushMatrix()

  #HEAD
  Pink()
  #Specify the x, y, and z coordinates of a translation vector.
  glTranslatef(0.0, head_x, 0.0)
  glRotatef(t1, 1.0, 0.0, 0.0)
  glRotatef(t2, 0.0, 1.0, 0.0)
  glTranslatef(0.0, head_y, 0.0)
  head()
#NOTE::for rendering every body part, similar rotate and translate(as shown above)
#instructions have been used. Hence I have not specifically pointed that out
#in the body parts modules that follow as it seemed redundant. 
  #LEFT UPPER ARM
  glPopMatrix()
  #  sets the rotations for dancing
  flag_dance=move[2]
  if(flag_dance==1):
  	rot_x=1.0
  	rot_y=0.0
  if(flag_dance==2):
  	rot_x=0.0
  	rot_y=1.0
  glPushMatrix()
  purple()
  glTranslatef(Left_U_arm_X, Left_U_arm_Y, 0.0)
  glRotatef(t3, rot_x, rot_y, 0.0)
  
  upper_arm()

  #LEFT LOWER ARM
  pink()
  glTranslatef(0.0, Left_L_arm_Y, 0.0)
  glRotatef(t4, 1.0, 0.0, 0.0)
  glRotatef(arm_rot[0], 0.0, 1.0, 1.0)
  lower_arm()

  #RIGHT UPPER ARM
  glPopMatrix()
  glPushMatrix()
  purple()
  glTranslatef(Right_U_arm_X, Right_U_arm_Y, 0.0)
  glRotatef(t5, 1.0, 0.0, 0.0)
  upper_arm()

  #RIGHT LOWER ARM
  pink()
  glTranslatef(0.0, Right_L_arm_Y, 0.0)
  glRotatef(t6, 1.0, 0.0, 0.0)
  glRotatef(arm_rot[1], 0.0, 0.0, 1.0)
  lower_arm()

  #LEFT UPPER LEG
  glPopMatrix()
  glPushMatrix()
  red()
  glTranslatef(Left_U_Leg_X, Left_U_Leg_Y, 0.0)
  glRotatef(t7, 1.0, 0.0, 0.0)
  upper_leg()

  #LEFT LOWER LEG
  blue()
  glTranslatef(0.0, Left_Lower_Leg_Y, 0.0)
  glRotatef(t8, 1.0, 0.0, 0.0)
  lower_leg()

  #RIGHT UPPER LEG
  glPopMatrix()
  glPushMatrix()
  red()
  glTranslatef(Right_U_Leg_X, Right_U_Leg_Y, 0.0)
  glRotatef(t9, 1.0, 0.0, 0.0)
  upper_leg()

  #RIGHT LOWER LEG
  blue()
  glTranslatef(0.0, Right_L_Leg_Y, 0.0)
  glRotatef(t10, 1.0, 0.0, 0.0)
  lower_leg()

  glPopMatrix()
  glFlush()
#function used for drawing basic primitive for torso
def torso():
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  #Draw Cylinder.
  gluCylinder(p, Torso_r, Torso_r, Torso_ht, 100, 100)
  glPopMatrix()
#function used for drawing basic primitive for head
def head():
  glPushMatrix()
  glRotatef(90, 1.0, 0.0, 0.0)
  glutWireSphere(0.1, 100, 100)
  glPopMatrix()
 #function used for drawing basic primitive for upper arm 
def upper_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*U_arm_h, 0.0)
  glScalef(U_arm_w, U_arm_h, U_arm_w)
  glutSolidCube(1.0)
  glPopMatrix()
#function used for drawing basic primitive for lower arm
def lower_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*U_arm_h, 0.0)
  glScalef(L_arm_w, L_arm_h, L_arm_w)
  glutSolidCube(1.0)
  glPopMatrix()
#function used for drawing basic primitive for upper leg
def upper_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*L_arm_h, 0.0)
  glScalef(U_leg_w, U_leg_h, U_leg_w)
  glutSolidCube(1.0)
  glPopMatrix()
#function used for drawing basic primitive for lower leg
def lower_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*L_arm_h, 0.0)
  glScalef(L_leg_w, L_leg_h, L_leg_w)
  glutSolidCube(1.0)
  glPopMatrix()
#simple functions to define colour RGB values
def red():
  glColor3f(1.0, 0.0, 0.0)

def purple():
  glColor3f(1.0, 0.5, 1.0)

def blue():
  glColor3f(0.0, 0.0, 1.0)

def cyan():
  glColor3f(0.0, 1.0, 1.0)


#change head/leg color.
def Pink():
  glColor3f(1.5, 1.0, 0.5)

def pink():
  glColor3f(1, 0, 1)

#change torso color.
def green():
  glColor3f(0, 1.0, 0)
  
  

#To compute the angle for rotation of body parts at various time instants 
def getAngle(freq,minimum,maximum,t):
        return (maximum-minimum)*math.sin(freq*3.14*t)+0.5*(maximum+minimum)
#Definition of Glut provided idle function
#Once action chosen, idle executes the action without any input at every instant
#It gets time and according to the action, sets the rotation angles for
#various body parts at different instants of time
def idle():
        seconds=glutGet(GLUT_ELAPSED_TIME)/1000.0
        global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, angle,x1,y1,z1,x2,y2,z2
        #For random dance, sets angles for rotation of arms and legs
        if(move[2]!=0):
        		t3 = getAngle(roangle_freq[3], roangle_min[3],roangle_max[3], seconds)
        		t5 = getAngle(roangle_freq[5], roangle_min[5],roangle_max[5], seconds)
        		t7 = getAngle(roangle_freq[7], roangle_min[7],roangle_max[7], seconds)
        		t9 = getAngle(roangle_freq[9], roangle_min[9],roangle_max[9], seconds)
        		t1 = getAngle(roangle_freq[1], roangle_min[1],roangle_max[1], seconds)
        		t4 = getAngle(roangle_freq[4], roangle_min[4],roangle_max[4], seconds)
        		t6 = getAngle(roangle_freq[6], roangle_min[6],roangle_max[6], seconds)
        		t0 = getAngle(roangle_freq[0], roangle_min[0],roangle_max[0], seconds)
        		
        #For shaking hands ala rajesh khanna, sets rotation angles for arms
        if (move[0]!=0):
                tpar[0]=0.0
                tpar[1]=0.0
                t3=0.0
                t4=270.0
                arm_rot[0]=getAngle(roangle_freq[6], roangle_min[6],roangle_max[6], seconds)
                t6=270.0
                t5 = 90.0
                arm_rot[1] = getAngle(roangle_freq[6], roangle_min[6],roangle_max[6], seconds)
        #For stopping all moves
        if (move[1]!=0):
                arm_rot[0]=0.0
                arm_rot[1]=0.0
                
                
        glutPostRedisplay()
        
#definition for glut provided keyboard function
#caps lock letters are for moving in direction opposite to that of lower case letters
def mykey(key, x, y):
  global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, angle,x1,y1,z1,x2,y2,z2
  if key == chr(27):#esc key to exit
      import sys
      sys.exit(0)
  if key=='d': # to move/rotate TORSO and hence whole body
    t0 = t0 + 10.0
      
  elif key=='D':#move in opposite direction
    t0 = t0 - 10.0
   
   
 
      
  elif key=='s': # Left Upper Arm
    t3 = t3 + 10.0
      
  elif key=='S':
    t3 = t3 - 10.0
      
  elif key=='a': # Left Lower Arm
    t4 = t4 + 10.0
      
  elif key=='A':
    t4 = t4 - 10.0
      
  elif key=='f': # Right Upper Arm
    t5 = t5 + 10.0
      
  elif key=='F':
    t5 = t5 - 10.0
      
  elif key=='g': # Right Lower Arm
    t6 = t6 + 10.0
      
  elif key=='G':
    t6 = t6 -10.0
      
  elif key=='k': # Left Upper Leg
    t7 = t7 + 10.0
      
  elif key=='K':
    t7 = t7 - 10.0
      
  elif key=='z': # Left Lower Leg
    t8 = t8 + 10.0
      
  elif key=='Z':
    t8 = t8 -10.0
      
  elif key=='u': # Right Upper Leg
    t9 = t9 + 10.0
      
  elif key=='U':
    t9 = t9 - 10.0
      
  elif key=='v': # Right Lower Leg
    t10 = t10 + 10.0
      
  elif key=='V':
    t10 = t10 - 10.0
      

  #Change Viewing(eye) angle. Move away from user if `u` key is pressed.
  elif key=='c':
          x1,y1,z1=x1+1,y1+1,z1+1
  #Move closer to user if 'U' is pressed.
  elif key=='C':
          x1,y1,z1=x1-1,y1-1,z1-1

  elif key=='j':# change view along x axis
          x2=x2+1
  elif key == 'J':
          x2=x2-1

  elif key=='l':# change view along z axis
          z2=z2+1
  elif key=='L':
          z2=z2-1
  #moves
  elif key=='h':#shake hands
  	move[2]=0
  	move[0]=1
  	move[1]=0
  elif key=='b':#stop move
  	move[2]=0
  	move[0]=0
  	move[1]=1
  elif key=='i':#random dance
  	move[2]=1
  	move[0]=0
  	move[1]=0
 
  elif key=='q':#raise hand and wave hi
    t3=310.0
    for x in range(0, 3000):
    	t4=t4 + 10.0


  
  glutPostRedisplay()
  

#    
glutInit( sys.argv )
glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB )
glutInitWindowSize( 500, 500 )
glutInitWindowPosition(0,0)
glutCreateWindow( 'Humanoid' )
glutDisplayFunc( display )
glutIdleFunc(idle)
glutKeyboardFunc(mykey)
p=gluNewQuadric()
gluQuadricDrawStyle(p, GLU_LINE)

glClearColor(0.0, 0.0, 0.0, 0.0)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(10, 1.0, 10.0, 100.0)

glutMainLoop()
