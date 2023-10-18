#include <math.h>
#include <iostream>

using namespace std;

float dx, dy, pk, step;

// fungsi brensenham
float steps(float  dx, float dy){
	float abs_dx = abs(dx);
	float abs_dy = abs(dy);
	
	if (abs_dx >= abs_dy){
		return abs_dx;
	} else{
		return abs_dy;
	}
}


void bresenhamLine(float x0, float y0, float x1, float y1){
	
	// step 1
	dx = x1 - x0;
	dy = y1 - y0;
	
	// step 2
	pk = (2*dy)-dx;
	
	// decide steps
	step = steps(dx, dy);
	
	cout <<"xk+1" << " yk+1" << endl;
	
	
	for (int i = 0; i < step+1; i++){
		cout << round(x0) << "     " << round(y0) << endl;
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
	
}

int main(){
	
	
	int x0 = 2, y0 = 9, x1 = 7, y1 = 2;
	-
	cout << "A(2, 9)" << endl;
	cout << "B(7, 2)" << endl;
	cout << endl;
	
	bresenhamLine(x0, y0, x1, y1);
	
	return 0;
}
