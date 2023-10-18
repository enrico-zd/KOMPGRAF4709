#include<GL/glut.h>
#include <math.h>
#include <iostream>

using namespace std;
// fungsi brensenham
float bresenham(float  dx, float dy){
	float abs_dx = abs(dx);
	float abs_dy = abs(dy);
	
	if (abs_dx >= abs_dy){
		return abs_dx;
	} else{
		return abs_dy;
	}
}

void garis();
main (int argc, char** argv)
{ 
	glutInit(&argc,argv); 
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB); 
	glutInitWindowSize(1200.0,720.0); 
	glutInitWindowPosition(0,0); 
	glutCreateWindow("Project Membuat Garis"); 
	glClearColor(0.0, 0.0, 0.0, 0.0); 
	glMatrixMode(GL_PROJECTION); 
	glOrtho(0.0f, 1200.0f, 720.0f, 0.0f, 0.0f, 1.0f); 
	glutDisplayFunc(garis); 
	glutMainLoop();
	
	
}

void garis()
{ 
	glClear(GL_COLOR_BUFFER_BIT); 
	glBegin(GL_LINES); 
	
	glColor3ub(255, 0, 0); 
	
	int x0 = 12, y0 = 1, x1 = 2, y1 = 8;
	
	glVertex2f(x0*100, y0*100); 
	// step 1
	float dx = x1 - x0;
	float dy = y1 - y0;
	
	// gradien
	float m = dy/dx;
	
	// step 2
	float steps = bresenham(dx, dy);
	
	for (int i = 0; i < steps; i++){
		x0 = round(x0 - 1);
		y0 = round(y0 - m);
		
	}
	
	-
	glVertex2f(2*100, y0*100);
	
	glPointSize(50.0f); 
	glEnd(); 
	glFlush();
}
