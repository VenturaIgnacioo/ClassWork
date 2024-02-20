#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NPALABRAS 10

int main(void) {
    // Defino el vector de punteros
    char *palabras[NPALABRAS];

    // Defino el resto de las variables
    char palabra[50];  // Asumo que ninguna palabra excede los 50 caracteres

    // Leo las palabras
    printf("Ingresa 10 palabras:\n");
    for (int i = 0; i < NPALABRAS; i++) {
        scanf("%s", palabra);
        palabras[i] = malloc(strlen(palabra) + 1);  // Reserva dinámica de memoria
        strcpy(palabras[i], palabra);
    }

    // Muestro la lista tal cual
    printf("\nLista tal cual:\n");
    for (int i = 0; i < NPALABRAS; i++) {
        printf("%s\n", palabras[i]);
    }

    // Ordeno la lista por su longitud (Bubble Sort)
    for (int i = 0; i < NPALABRAS - 1; i++) {
        for (int j = 0; j < NPALABRAS - i - 1; j++) {
            if (strlen(palabras[j]) > strlen(palabras[j + 1])) {
                // Intercambio de punteros
                char *temp = palabras[j];
                palabras[j] = palabras[j + 1];
                palabras[j + 1] = temp;
            }
        }
    }

    // Vuelvo a mostrar la lista
    printf("\nLista ordenada por longitud:\n");
    for (int i = 0; i < NPALABRAS; i++) {
        printf("%s\n", palabras[i]);
    }

    // Liberar memoria
    for (int i = 0; i < NPALABRAS; i++) {
        free(palabras[i]);
    }

    return 0;
}
