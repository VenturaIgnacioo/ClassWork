#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

#define MAX_LONGITUD_PALABRA 50
#define NUM_PALABRAS 5

// Declaración de funciones
void leerPalabras(char* palabras[NUM_PALABRAS]);
void verificarLongitudPalabra(char* palabra);
int contarConsonantes(const char* palabra);
void ordenarPalabrasPorConsonantes(char* palabras[NUM_PALABRAS]);
char* reemplazarVocales(char* palabra);

int main() {
    char* palabras[NUM_PALABRAS];

    // Leer palabras
    leerPalabras(palabras);

    // Verificar y repetir si una palabra tiene más de 10 letras
    for (int i = 0; i < NUM_PALABRAS; ++i) {
        verificarLongitudPalabra(palabras[i]);
    }

    // Ordenar palabras por el número de consonantes
    ordenarPalabrasPorConsonantes(palabras);

    // Reemplazar vocales en cada palabra
    for (int i = 0; i < NUM_PALABRAS; ++i) {
        reemplazarVocales(palabras[i]);
    }

    // Mostrar las palabras modificadas
    printf("Palabras modificadas:\n");
    for (int i = 0; i < NUM_PALABRAS; ++i) {
        printf("%s\n", palabras[i]);
    }

    // Liberar memoria asignada
    for (int i = 0; i < NUM_PALABRAS; ++i) {
        free(palabras[i]);
    }

    return 0;
}

void leerPalabras(char* palabras[NUM_PALABRAS]) {
    printf("Ingrese 5 palabras:\n");
    for (int i = 0; i < NUM_PALABRAS; ++i) {
        palabras[i] = (char*)malloc(MAX_LONGITUD_PALABRA * sizeof(char));
        scanf("%s", palabras[i]);
    }
}

void verificarLongitudPalabra(char* palabra) {
    while (strlen(palabra) > 10) {
        printf("La palabra tiene más de 10 letras. Ingrese una nueva palabra: ");
        scanf("%s", palabra);
    }
}

int contarConsonantes(const char* palabra) {
    int consonantes = 0;
    for (int i = 0; palabra[i] != '\0'; ++i) {
        char letraActual = tolower(palabra[i]);
        if (isalpha(letraActual) && letraActual != 'a' && letraActual != 'e' &&
            letraActual != 'i' && letraActual != 'o' && letraActual != 'u') {
            consonantes++;
        }
    }
    return consonantes;
}

void ordenarPalabrasPorConsonantes(char* palabras[NUM_PALABRAS]) {
    // Método de burbuja
    for (int i = 0; i < NUM_PALABRAS - 1; ++i) {
        for (int j = 0; j < NUM_PALABRAS - i - 1; ++j) {
            if (contarConsonantes(palabras[j]) > contarConsonantes(palabras[j + 1])) {
                // Intercambiar palabras
                char* temp = palabras[j];
                palabras[j] = palabras[j + 1];
                palabras[j + 1] = temp;
            }
        }
    }
}

char* reemplazarVocales(char* palabra) {
    srand(time(NULL));
    for (int i = 0; palabra[i] != '\0'; ++i) {
        char letraActual = tolower(palabra[i]);
        if (letraActual == 'a' || letraActual == 'e' || letraActual == 'i' ||
            letraActual == 'o' || letraActual == 'u') {
            // Reemplazar con una vocal aleatoria
            char substitutos[] = {'*', '_', 'ñ', 'Ø'};
            palabra[i] = substitutos[rand() % 4];
        }
    }
    return palabra;
}
