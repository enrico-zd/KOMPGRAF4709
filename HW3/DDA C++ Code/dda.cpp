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

// fungsi soal 1
float soal1(float xp, float yp, float steps, float m){
	
	for (int i = 0; i < steps; i++){
		xp -= 1;
		yp -= m;
		cout << round(xp) << " " << round(yp) << endl;
	}
}

// fungsi soal 2
float soal2(float xp, float yp, float steps, float m){
	
	for (int i =0; i < steps; i++){
		xp += 1;
		yp += m;
		cout << round(xp) << " " << round(yp) << endl;
	}
}

void DDA(string soal, float x0, float y0, float x1, float y1){
	
	// step 1
	float dx = x1 - x0;
	float dy = y1 - y0;
	
	// gradien
	float m = dy/dx;
	
	// step 2
	float steps = bresenham(dx, dy);
	
	// step 3
	if (soal == "satu"){
		soal1(x0, y0, steps, m);
	}
	else if (soal == "dua"){
		soal2(x0, y0, steps, m);
	}
	
}

int main(){
	
	// soal
	string soal;
	
	int x01 = 12, y01 = 1, x11 = 2, y11 = 8;
	
	cout << "Soal No. 1" << endl;
	cout << "A(12, 1)" << endl;
	cout << "B(2, 8)" << endl;
	cout << endl;
	
	DDA(soal="satu", x01, y01, x11, y11);
	 
	cout << endl;
	 
	// soal 2
	int x02 = 2, y02 = 12, x12 = 4, y12 = 10;
	
	cout << "Soal No. 2" << endl;
	cout << "A(2, 12)" << endl;
	cout << "B(4, 10)" << endl;
	
	DDA(soal="dua", x02, y02, x12, y12);
	
	return 0;
}
