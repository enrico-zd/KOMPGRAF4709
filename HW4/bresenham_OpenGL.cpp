#include<GL/glut.h>
#include<stdlib.h>
#include<stdio.h>


 
void display(void)
{
float x0=1,xn=7,y0=2,yn=2;	

float dy,dx,x,y,p,duady,duadydx,xend;

// mencari dx dan dy
dx=abs(xn-x0);
dy=abs(yn-y0);

// hitung p
p = 2 * dx - dy;
duady = 2 * dy;
duadydx = 2 * (dy - dx);

// tentukan titik awal dan titik akhir
if (x0 > xn){
	x = xn;
	y = yn;
	xend = x0;
} else{
	x = x0;
	y = y0;
	xend = xn;
}

// gambar titik awal
glPointSize(5);
glBegin(GL_POINTS);
glVertex2i(x,y);

// perulangan untuk menggambar titik-titik
while (x < xend){
	x++;
	if (p < 0){
		p += duady;
	} else{
		if (y0 > yn){
			y--;
		} else if (y0 == yn){
			y=y;
		}else{
			y++;
		}
		p += duadydx;
	}
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
glutCreateWindow ("Bresenham Line Algo");
init();
glutDisplayFunc(display);
glutMainLoop();
 
return 0;
}


