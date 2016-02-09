#!/usr/bin/python
#Name:Devanshi Vyas
#ID no.201101141
#This Program creates a wire cube with a list of vertices and individually makes each face
#using a separate function and when user presses t,truncates
#the corners one by one,re-rendering the faces. One can also rotate it using a,s,w,d keys.

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception
#import libraries
import sys


try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''
ERROR: PyOpenGL not installed properly.  
        '''
#initializing values for the vertices
#a is the original vertex,b gives how much of the edge is to be cut
#c gives what is left.
#cut keeps a count of the number of corners truncated
#h and v are for rotation about the axes
a = 1
b = 0.4
c = a - b
cut = 0
h = 0.0
v = 0.0

#original vertices of the cube
v0 = [0,0,0]
v1 = [a,0,0]
v2 = [0,a,0]
v3 = [a,a,0]
v4 = [0,0,a]
v5 = [a,0,a]
v6 = [0,a,a]
v7 = [a,a,a]


# vertices when corner 0 is cut(to replace v0)
v01 = [b,0,0]
v02 = [0,b,0]
v04 = [0,0,b]

# vertices when corner 1 is cut(to replace v1)
v10 = [c,0,0]
v13 = [a,b,0]
v15 = [a,0,b]

# vertices when corner 2 is cut(to replace v2)
v20 = [0,c,0]
v23 = [b,a,0]
v26 = [0,a,b]

# vertices when corner 3 is cut(to replace v3)
v31 = [a,c,0]
v32 = [c,a,0]
v37 = [a,a,b]

# vertices when corner 4 is cut(to replace v4)
v40 = [0,0,c]
v45 = [b,0,a]
v46 = [0,b,a]

# vertices when corner 5 is cut(to replace v5)
v51 = [a,0,c]
v54 = [c,0,a]
v57 = [a,b,a]

# vertices when corner 6 is cut(to replace v6)
v62 = [0,a,c]
v64 = [0,c,a]
v67 = [b,a,a]

# vertices when corner 7 is cut(to replace v7)
v73 = [a,a,c]
v75 = [a,c,a]
v76 = [c,a,a]

# Clears screen and sets shading model  
def init(): 
   glClearColor (0.0, 0.0, 0.0, 0.0)
   glShadeModel (GL_FLAT)

#function to draw face0. Depending on the number of cuts, it draws
#either the original corner vertex or the 2 points which replace it.
def draw_face0():

   glBegin(GL_LINE_LOOP)
   if cut>=8:
           glVertex3fv(v02)
           glVertex3fv(v01)
   else:
           glVertex3fv(v0)
   if cut>=7:
           glVertex3fv(v10)
           glVertex3fv(v13)
   else:
           glVertex3fv(v1)
   if cut>=5:
           glVertex3fv(v31)
           glVertex3fv(v32)
   else:
           glVertex3fv(v3)
   if cut>=6:
           glVertex3fv(v23)
           glVertex3fv(v20)
   else:
           glVertex3fv(v2)
   glEnd()  
   
#function to draw face1. Depending on the number of cuts, it draws
#either the original corner vertex or the 2 points which replace it on the face.      
def draw_face1():

   glBegin(GL_LINE_LOOP)
   if cut>=8:
           glVertex3fv(v04)
           glVertex3fv(v02)
   else:
           glVertex3fv(v0)
   if cut>=6:
           glVertex3fv(v20)
           glVertex3fv(v26)
   else:
           glVertex3fv(v2)
   if cut>=2:
           glVertex3fv(v62)
           glVertex3fv(v64)
   else:
           glVertex3fv(v6)
   if cut>=4:
           glVertex3fv(v46)
           glVertex3fv(v40)
   else:
           glVertex3fv(v4)
   glEnd()
   
#function to draw face2. Depending on the number of cuts, it draws
#either the original corner vertex or the 2 points which replace it on the face.     
def draw_face2():

   glBegin(GL_LINE_LOOP)
   if cut>=8:
           glVertex3fv(v04)
           glVertex3fv(v01)
   else:
           glVertex3fv(v0)
   if cut>=7:
           glVertex3fv(v10)
           glVertex3fv(v15)
   else:
           glVertex3fv(v1)
   if cut>=3:
           glVertex3fv(v51)
           glVertex3fv(v54)
   else:
           glVertex3fv(v5)
   if cut>=4:
           glVertex3fv(v45)
           glVertex3fv(v40)
   else:
           glVertex3fv(v4)
   glEnd()
   
#function to draw face3. Depending on the number of cuts, it draws
#either the original corner vertex or the 2 points which replace it on the face.     
def draw_face3():

   glBegin(GL_LINE_LOOP)
   if cut>=1:
           glVertex3fv(v75)
           glVertex3fv(v76)
   else:
           glVertex3fv(v7)
   if cut>=2:
           glVertex3fv(v67)
           glVertex3fv(v64)
   else:
           glVertex3fv(v6)
   if cut>=4:
           glVertex3fv(v46)
           glVertex3fv(v45)
   else:
           glVertex3fv(v4)
   if cut>=3:
           glVertex3fv(v54)
           glVertex3fv(v57)
   else:
           glVertex3fv(v5)
   glEnd()
   
#function to draw face4. Depending on the number of cuts, it draws
#either the original corner vertex or the 2 points which replace it on the face.     
def draw_face4():

   glBegin(GL_LINE_LOOP)
   if cut>=1:
           glVertex3fv(v73)
           glVertex3fv(v75)
   else:
           glVertex3fv(v7)
   if cut>=3:
           glVertex3fv(v57)
           glVertex3fv(v51)
   else:
           glVertex3fv(v5)
   if cut>=7:
           glVertex3fv(v15)
           glVertex3fv(v13)
   else:
           glVertex3fv(v1)
   if cut>=5:
           glVertex3fv(v31)
           glVertex3fv(v37)
   else:
           glVertex3fv(v3)
   glEnd()
   
#function to draw face5. Depending on the number of cuts, it draws
#either the original corner vertex or the 2 points which replace it on the face.     
def draw_face5():

   glBegin(GL_LINE_LOOP)
   if cut>=1:
           glVertex3fv(v73)
           glVertex3fv(v76)
   else:
           glVertex3fv(v7)
   if cut>=2:
           glVertex3fv(v67)
           glVertex3fv(v62)
   else:
           glVertex3fv(v6)
   if cut>=6:
           glVertex3fv(v26)
           glVertex3fv(v23)
   else:
           glVertex3fv(v2)
   if cut>=5:
           glVertex3fv(v32)
           glVertex3fv(v37)
   else:
           glVertex3fv(v3)
   glEnd()

#function to draw the cube by calling individual functions to draw the 6 faces independently.    
def draw_cube():
   draw_face0()
   draw_face1()
   draw_face2()
   draw_face3()
   draw_face4()
   draw_face5()

#primary display function to draw the cube and rotate it if desired.
def display():
   glClear (GL_COLOR_BUFFER_BIT)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()

   glFrustum(-1.0, 1.0, -1.0, 1.0, 1, 5.0)
   glMatrixMode(GL_MODELVIEW)

   # clear the matrix
   glLoadIdentity()              
   # viewing transformation 
   gluLookAt (0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

   glColor3f (1.0, 1.0, 1.0)
   glRotatef(h, 0.0, 1.0, 0.0)
   glRotatef(v, 1.0, 0.0, 0.0)
   glTranslatef(-0.5, -0.5, -0.5)
   draw_cube()
   glFlush ()

#definition of the glut provided keyboard function
def keyboard(key, x, y):
   global h, v, cut
   if key == chr(27):#esc key to exit
      import sys
      sys.exit(0)
   elif key == 'w':#rotate vertically
      v = v - 10.0
   elif key == 's':#rotate in opp direction
      v = v + 10.0
   elif key == 'a':#rotate horizontally
      h = h - 10.0
   elif key == 'd':#rotate in opp direction
      h = h + 10.0
   elif key == 't':#truncate a corner
      cut = cut + 1.0
   glutPostRedisplay()   

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ('cube')
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
