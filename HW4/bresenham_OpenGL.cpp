#include<GL/glut.h>
#include <math.h>
#include <iostream>

float dx, dy, pk, step;

float steps(float  dx, float dy){
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
	
	int x0 = 2, y0 = 9, x1 = 7, y1 = 2;
	
	// titik awal
	glVertex2f(x0*100, y0*100); 
	
	// step 1
	dx = x1 - x0;
	dy = y1 - y0;
	
	// step 2
	pk = (2*dy)-dx;
	
	// decide steps
	step = steps(dx, dy);
	
	
	for (int i = 0; i < step+1; i++){
		if (pk < 0){
			pk = pk + abs(2*dy);
			x0 = x0;
			y0 = y0 -1;
		} 
		else if (pk >= 0){
			pk = pk + abs(2*dy)-abs(2*dx);
			x0 = x0+1;
			y0 = y0-1;
		}
	}
	
	// titik akhir
	glVertex2f(x0*100, y0*100);
	
	glPointSize(50.0f); 
	glEnd(); 
	glFlush();
}
