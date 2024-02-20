#include <stdio.h>

int verificarTresEnRaya(char matriz[3][3]) {
    // Verificar filas y columnas
    for (int i = 0; i < 3; ++i) {
        if ((matriz[i][0] == matriz[i][1] && matriz[i][1] == matriz[i][2]) ||
            (matriz[0][i] == matriz[1][i] && matriz[1][i] == matriz[2][i])) {
            if (matriz[i][i] == 'O') {
                return 1; // Las O forman 3 en raya
            } else if (matriz[i][i] == 'X') {
                return -1; // Las X forman 3 en raya
            }
        }
    }

    // Verificar diagonales
    if ((matriz[0][0] == matriz[1][1] && matriz[1][1] == matriz[2][2]) ||
        (matriz[0][2] == matriz[1][1] && matriz[1][1] == matriz[2][0])) {
        if (matriz[1][1] == 'O') {
            return 1; // Las O forman 3 en raya
        } else if (matriz[1][1] == 'X') {
            return -1; // Las X forman 3 en raya
        }
    }

    return 0; // Ningún jugador forma 3 en raya
}

int main() {
    char tablero[3][3] = {
        {'O', 'X', 'O'},
        {'X', 'O', 'X'},
        {'O', 'X', 'O'}
    };

    int resultado = verificarTresEnRaya(tablero);
    printf("Resultado: %d\n", resultado);

    return 0;
}
