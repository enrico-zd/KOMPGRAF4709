#include<GL/glut.h>
#include<stdlib.h>
#include<stdio.h>

 
void display(void)
{
	float x1 = 1,x2 = 7,y1 = 2,y2 = 2;	

	float dy,dx,step,x,y,k,Xin,Yin;
	
	x = x1;
	y = y1;
	
	// mencari dx dan dy
	dx=x2-x1;
	dy=y2-y1;

	// steps 
	if(abs(dx)> abs(dy))
	{
		step = abs(dx);	
	}
	else
		step = abs(dy);
	 	
	 	// mencari nilai increment
		Xin = dx/step;
		Yin = dy/step;
		
		glPointSize(5);
		glBegin(GL_POINTS);
		
		glVertex2i(x,y);
		glEnd();
	 
	for (k=1 ;k<=step;k++)
	{
		x= x + Xin;
		y= y + Yin;
		 
		glBegin(GL_POINTS);
		glVertex2i(x,y);
		glEnd();
	}
	 
	 
	glFlush();
}
 
void init(void)
{
	glClearColor(0.7,0.7,0.7,0.7);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-5,30,-5,30);
}
 
int main(int argc, char** argv) {
 
	glutInit(&argc, argv);
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize (500, 500);
	glutInitWindowPosition (100,100);
	glutCreateWindow ("DDA Line Algo");
	init();
	glutDisplayFunc(display);
	glutMainLoop();
	 
	return 0;
}


