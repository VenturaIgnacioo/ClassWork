package miCodigo;

import java.util.Scanner;

public class ManejaAlumnos {

   public static void main(String[] args) {
       // TODO Auto-generated method stub
       Scanner entrada = new Scanner(System.in);
       Alumno clase[];
       clase=new Alumno[3];


       for(int cont=0;cont<3;cont++) {
           clase[cont]=new Alumno();
           System.out.println("Nombre alumno "+cont);
           clase[cont].setNombre(entrada.next());
           System.out.println("Primer apellido alumno "+cont);
           clase[cont].setApellido1(entrada.next());
           System.out.println("Segundo apellido alumno "+cont);
           clase[cont].setApellido2(entrada.next());
           System.out.println("Nota alumno "+cont);
           clase[cont].setNota(entrada.nextDouble());
       }
       System.out.println("****************************");
       System.out.println("* LISTA DE CLASE *");
       System.out.println("****************************");
       for(int cont=0;cont<3;cont++) {
           System.out.print("\n"+(cont+1)+". ");
           System.out.print(clase[cont].getNombre()+" ");
           System.out.print(clase[cont].getApellido1()+" ");
           System.out.print(clase[cont].getApellido2()+" ");
           System.out.print(clase[cont].getNota());
           
       }

   }

}
