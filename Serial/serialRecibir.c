#include <18F4550.h>                     //Incluimos la librer�a 18F455
#device ADC=10                         
#fuses HS, NOWRT, NOWDT,NOPROTECT, NOPUT, NOLVP 
#use delay(crystal=8000000)             
#include <stdlib.h>                     

#BYTE PORTB = 0xF81                   
#BYTE TRISB = 0xF93                      

#use RS232(baud=9600,bits=8,parity=N,xmit=pin_c6,rcv=pin_c7)


int dato =0;

#int_rda                                 //Habilita la funci�n de interrupci�n por recepci�n de datos 
void rda_isr()                           //Funci�n de interrupci�n recepci�n de datos.
{
   dato=getc();                          //Asigna el valor de recepci�n a la variable dato.
  
}
void main (){
   enable_interrupts(int_rda);           //Habilitamos la interrupci�n por recepci�n
   enable_interrupts(GLOBAL);  

   while(true){
      if (dato==0){
         output_toggle(PIN_B1);
      }
   }
}
