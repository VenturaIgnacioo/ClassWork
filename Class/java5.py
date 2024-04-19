package miCodigo;

public class ManejaPersona {

   public static void main(String[] args) {
       // TODO Auto-generated method stub
       Persona alumnos[];
       alumnos=new Persona[3];
       alumnos[0]=new Persona("Martinez","Ruiz","Marcos");
       alumnos[1]=new Persona("Cervantes","Alcaine","Juan");
       alumnos[2]=new Persona("Fernandez","Hernandez","Adriana");
       for(int cont=0;cont<3;cont++) {
           System.out.println("\n- "+alumnos[cont].getNombreCompleto());    
           
       }
   }

}
