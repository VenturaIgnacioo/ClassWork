/**
 *
 */
package miCodigo;

/**
 * Esta clase guarda información sobre los datos de una persona
 */
public class Persona {
    private String nombre;
    private String apellido1;
    private String apellido2;
    private int edad;
    private String telefono;
    private float notaTIC;
    private boolean usaComedor;
    /**
     * @param apellido1
     * @param apellido2
     * @param nombre
     */
    public Persona(String apellido1, String apellido2, String nombre) {
        this.apellido1 = apellido1;
        this.apellido2 = apellido2;
        this.nombre = nombre;
    }
    /**
     * @param apellido1
     */
    public Persona(String apellido1) {
        this.apellido1 = apellido1;
    }    
   
   
    /**
     * @return the nombre
     */
    public String getNombre() {
        return nombre;
    }
    /**
     * @param nombre the nombre to set
     */
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    /**
     * @return the apellido1
     */
    public String getApellido1() {
        return apellido1;
    }
    /**
     * @param apellido1 the apellido1 to set
     */
    public void setApellido1(String apellido1) {
        this.apellido1 = apellido1;
    }
    /**
     * @return the apellido2
     */
    public String getApellido2() {
        return apellido2;
    }
    /**
     * @param apellido2 the apellido2 to set
     */
    public void setApellido2(String apellido2) {
        this.apellido2 = apellido2;
    }
    /**
     * @return the edad
     */
    public int getEdad() {
        return edad;
    }
    /**
     * @param edad the edad to set
     */
    public void setEdad(int edad) {
        this.edad = edad;
    }
    /**
     * @return the telefono
     */
    public String getTelefono() {
        return telefono;
    }
    /**
     * @param telefono the telefono to set
     */
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    /**
     * @return the notaTIC
     */
    public float getNotaTIC() {
        return notaTIC;
    }
    /**
     * @param notaTIC the notaTIC to set
     */
    public void setNotaTIC(float notaTIC) {
        this.notaTIC = notaTIC;
    }
    /**
     * @return the usaComedor
     */
    public boolean isUsaComedor() {
        return usaComedor;
    }
    /**
     * @param usaComedor the usaComedor to set
     */
    public void setUsaComedor(boolean usaComedor) {
        this.usaComedor = usaComedor;
    }
   
    String getNombreCompleto() {
        String respuesta;
        respuesta=nombre+" "+apellido1+" "+apellido2;
        return(respuesta);
       
    }
    String getEdadAnios() {
       
        return(edad+" años");
    }    
   
   
   

}
