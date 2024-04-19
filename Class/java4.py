package miCodigo;

public class Circulo {
   int coordX;
   int coordY;
   int radio;
   
   Circulo(int coordXEnviada,int coordYEnviada,int radioEnviado){
       coordX=coordXEnviada;
       coordY=coordYEnviada;
       radio=radioEnviado;    
       
   }
   
   double devuelveLongitudCirculo(){
       double respuesta;
       respuesta=2 * Math.PI*radio;
       return respuesta;
   }
   
   double devuelveArea(){
       double respuesta;
       respuesta= Math.PI*Math.sqrt(radio);
       return(respuesta);
   }

}
