package miCodigo;

public class MercanciaCaducidad extends Mercancia{
   private int dia;
   private int mes;
   private int anio;
   /**
    * @param nombre
    * @param precio
    * @param cod_proveedor
    * @param dia
    * @param mes
    * @param anio
    */
   public MercanciaCaducidad(String nombre, double precio, String cod_proveedor, int dia, int mes, int anio) {
       super(nombre, precio, cod_proveedor);
       this.dia = dia;
       this.mes = mes;
       this.anio = anio;
   }
   

}
