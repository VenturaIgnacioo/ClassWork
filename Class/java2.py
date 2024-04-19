package miCodigo;

import java.util.Scanner;

public class ManejaParejaNumeros {

   public static void main(String[] args) {
       int num1;
       int num2;
       Scanner entrada = new Scanner(System.in);
       ParejaNumeros miPareja;
       //miPareja es un nuevo objeto de la clase ParejaNumeros
       
       System.out.println("\nNumero 1: ");//Sacamos por consola un mensaje
       num1=entrada.nextInt();//leemos un número
       System.out.println("\nNumero 2: ");//Sacamos por consola un mensaje
       num2=entrada.nextInt();//leemos un número        
       
       
       miPareja=new ParejaNumeros(num1,num2);
       //Utilicemos el nuevo objeto
       System.out.println("La suma vale: ");
       System.out.println(miPareja.devuelveSuma());
       

   }

}
