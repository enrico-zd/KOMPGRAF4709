#include <iostream>
#include <stdio.h>
using namespace std;

void dis_matrix(int matrix[2][2]){
	for (int i = 0; i < 2; i++){
		for (int j = 0; j < 2; j++){
			cout << matrix[i][j] << " ";
		}
		cout << endl;
	}
}

int main(void){
	int A[2][2] = {{1, 2}, 
					{3, 4}};
			
	int B[2][2] = {{1, 0}, 
					{1, 0}};
				
	// input matrix	
	int C[2][2];
	cout << "Masukan elemen matrix:" << endl;
	for (int i = 0; i < 2; i++){
		for (int j=0; j < 2; j++){
			cin >> C[i][j];
		}
	}
		
					
	int tambahMatrix[2][2];
	int kurangMatrix[2][2];
	int inputMatrix[2][2];
	int kaliMatrix[2][2];
	int jumlah;
	
	// Penjumlahan Matrix
	for (int i = 0; i < 2; i++){
		for (int j = 0; j < 2; j++){
			tambahMatrix[i][j] = A[i][j] + B[i][j];
		}
	}
	
	// Pengurangan Matrix
	for (int i = 0; i < 2; i++){
		for (int j = 0; j < 2; j++){
			kurangMatrix[i][j] = A[i][j] - B[i][j];
		}
	}
	
	// Perkalian Matrix input data
	for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            inputMatrix[i][j] = 0;
            for (int k = 0; k < 2; k++) {
                inputMatrix[i][j] += A[i][k] * C[k][j];
            }
        }
    }
	
	// Perkalian Matrix
	for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            kaliMatrix[i][j] = 0;
            for (int k = 0; k < 2; k++) {
                kaliMatrix[i][j] += A[i][k] * B[k][j];
            }
        }
    }
	
	// Henampilkan Hasil Penghitungan Matrix
	cout << "A+B:" << endl;
	dis_matrix(tambahMatrix);
	cout << endl;
	
	cout << "A-B:" << endl;
	dis_matrix(kurangMatrix);
	cout << endl;
	
	cout << "A*(n)input"<< endl;
	dis_matrix(inputMatrix);
	cout << endl;
	
	cout << "A*B" << endl;
	dis_matrix(kaliMatrix);
	
	return 0;
}
