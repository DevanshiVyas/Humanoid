#Name:Devanshi Vyas
#ID no.201101141
# This program is based on the example given in the redbook chapter 2(end)
#It creates a geodesic sphere from primitive triangle,
#Using an icosahedron as an approximation for a sphere.
# An icosahedron is constructed and repeatedly subdivided to form a sphere,
# by calculating the midpoint of edges of each triangle. More the number
#of subdivisions,smoother is the sphere.Lighting has also been added.
# One can increase/decrease the radius(size) of the sphere and the number
#of subdivisions and enable/disable the lighting using keyboard input.
#P.S:As there is a lot of computation,it may take a while to load.Please be patient.

# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception
import sys
import random
import math
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print '''
ERROR: PyOpenGL not installed properly.  
        '''
# Clears screen and sets shading model  
def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_SMOOTH)
    
# Set up light properties
l_specular=[1.0,0.0,0.0,1.0]
l_diffuse=[1.0,1.0,1.0,1.0]
l_ambient=[0.4,0.4,0.4,1.0]
l_position=[-50.0,50.0,5.0,0.0]
    
#Set up material properties of the sphere
m_specular=[0.0,0.0,0.0,1.0]
m_diffuse=[0.8,0.8,0.4,1.0]
m_ambient=[1.0,0.5,0.4,1.0]
m_shininess=80.0



#Pos contains the vertices/co ordinates of the sphere
pos=[]
 
#para contains the radius and number of subdivisions 

para=[1,1]
flag=0

#Adds points to the array Pos which are rendered as points on the sphere
def addPoint(p):
    length=math.sqrt(p[0]*p[0]+p[1]*p[1]+p[2]*p[2])
    pos.append([p[0]/length,p[1]/length,p[2]/length])

#It takes two points as input
#Calclates the midpoint of the two points, and adds it to pos[] & returns its index
def midpoint(p1,p2):
    index=len(pos)
    mid=[]
    mid.append((p1[0]+p2[0])/2)
    mid.append((p1[1]+p2[1])/2)
    mid.append((p1[2]+p2[2])/2)
    addPoint(mid)
    return index

    
#Enables the light, sets light and material properties
def l_enable():
    glLightfv(GL_LIGHT0,GL_AMBIENT,l_ambient)
    glLightfv(GL_LIGHT0,GL_DIFFUSE,l_diffuse)
    glLightfv(GL_LIGHT0,GL_SPECULAR,l_specular)
    glMaterialfv(GL_FRONT,GL_SHININESS,m_shininess)
    glMaterialfv(GL_FRONT,GL_AMBIENT,m_ambient)
    glMaterialfv(GL_FRONT,GL_DIFFUSE,m_diffuse)
    glMaterialfv(GL_FRONT,GL_SPECULAR,m_specular)
    glLightfv(GL_LIGHT0,GL_POSITION,l_position)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    

#Disables Light
def l_disable():
        glDisable(GL_LIGHTING)

#Primary display function
#Creates the icosahedron, subdivides it, adds vertices to the position array
# and renders the sphere on the screen
def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glLoadIdentity ()
    # Stores indices of each triangle
    TIndices=[]
    gluLookAt (5.0, 5.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    # Radius is increased/decreased by scaling, para[0] contains radius value
    # and para[1] no. of subdivisions that is the recursion levels
    glScalef (para[0], para[0], para[0])    
    recursion_level=para[1]
    # Creating icosahedron. 
    # The vertices of icosahedron are the corners of three perpendicular planes
    #It has 20 triangular faces which are all equilateral triangles
    t = (1.0 + math.sqrt(5.0)) / 2.0
    r=1.0
    addPoint([-r,  t*r,  0])
    addPoint([ r,  t*r,  0])
    addPoint([-r, -t*r,  0])
    addPoint([ r, -t*r,  0])
    addPoint([ 0, -1*r,  t*r])
    addPoint([ 0,  1*r,  t*r])
    addPoint([ 0, -1*r, -t*r])
    addPoint([ 0,  1*r, -t*r])
    addPoint([ t*r,  0, -r])
    addPoint([ t*r,  0,  r])
    addPoint([-t*r,  0, -r])
    addPoint([-t*r,  0,  r])
    # Create equilateral triangles
    eqtri =[]
    eqtri.append([0, 11, 5])
    eqtri.append([0, 5, 1])
    eqtri.append([0, 1, 7])
    eqtri.append([0, 7, 10])
    eqtri.append([0, 10, 11])
    # 5 adjacent triangles
    eqtri.append([1, 5, 9])
    eqtri.append([5, 11, 4])
    eqtri.append([11, 10, 2])
    eqtri.append([10, 7, 6])
    eqtri.append([7, 1, 8])
    # 5 triangles around vertex 3
    eqtri.append([3, 9, 4])
    eqtri.append([3, 4, 2])
    eqtri.append([3, 2, 6])
    eqtri.append([3, 6, 8])
    eqtri.append([3, 8, 9])
    # 5 adjacent triangles
    eqtri.append([4, 9, 5])
    eqtri.append([2, 4, 11])
    eqtri.append([6, 2, 10])
    eqtri.append([8, 6, 7])
    eqtri.append([9, 8, 1])
    # Creates midpoint of each of the triangle points and adds new eqtri to eqtri[]
    for i in range (0,recursion_level):
        eqtri2 = []
        v1=0
        v2=1
        v3=2
	# Finds midpoints and creates four triangles from the new and old vertices 
	# which are then added to eqtri
        for tri in eqtri:
            a = midpoint(pos[tri[v1]], pos[tri[v2]])
            b = midpoint(pos[tri[v2]], pos[tri[v3]])
            c = midpoint(pos[tri[v1]], pos[tri[v3]])
            eqtri2.append([tri[v1], a, c])
            eqtri2.append([tri[v2], b, a])
            eqtri2.append([tri[v3], c, b])
            eqtri2.append([a, b, c])
        eqtri = eqtri2;
        # Adding triangles to the index array
        for  tri in eqtri:
            TIndices.append([tri[v1],tri[v2],tri[v3]])
    # Draw the triangles        
    for i in range (0,len(TIndices)):
        #reddish colour when light is enabled
        #random no. generated colors so that each triangle is coloured differently
        
        if(flag==1):
        	glColor3f(1.0,0.0,0.0)
        else:
        	glColor3f(random.random(),random.random(),random.random())
        glBegin(GL_TRIANGLES)#getting all the points of the icosahedron and normalizing them to form a smooth sphere
        glVertex3f(pos[TIndices[i][0]][0],pos[TIndices[i][0]][1],pos[TIndices[i][0]][2])
        glNormal3f(pos[TIndices[i][0]][0],pos[TIndices[i][0]][1],pos[TIndices[i][0]][2])
        glVertex3f(pos[TIndices[i][1]][0],pos[TIndices[i][1]][1],pos[TIndices[i][1]][2])
        glNormal3f(pos[TIndices[i][1]][0],pos[TIndices[i][1]][1],pos[TIndices[i][1]][2])
        glVertex3f(pos[TIndices[i][2]][0],pos[TIndices[i][2]][1],pos[TIndices[i][2]][2])
        glNormal3f(pos[TIndices[i][2]][0],pos[TIndices[i][2]][1],pos[TIndices[i][2]][2])
        glEnd()
    glFlush ()

# Resets the objects when window is resized
def reshape (w, h):
    glViewport (0, 0, w, h)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    glFrustum (-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode (GL_MODELVIEW)
    
#definition for the glut provided keyboard function
def mykey(key, x, y):
  
  if key == chr(27):#esc key to exit
      import sys
      sys.exit(0)
  if key=='i': #increase radius
  	if para[0]<=4:
  		para[0]=para[0]+1
    
      
  elif key=='d':#decrease radius
  	if para[0]>=1:
  		para[0]=para[0]-1
    
   
   # increase subdivisions
  elif key=='s':
  	if para[1]<=4:
  		para[1]=para[1]+1
      
  elif key=='r':#reduces subdivisions
  	if para[1]>=1:
  		para[1]=para[1]-1
    
    #add lighting  
  elif key=='a':
  	l_enable()
  	flag=1
      
  elif key=='h':#remove lighting
  	l_disable()
  	flag=0
  glutPostRedisplay()
  

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (500, 500)
glutInitWindowPosition (100, 100)
glutCreateWindow ('Sphere')
init ()
glutKeyboardFunc(mykey)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
