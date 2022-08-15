#include <main.h>
#include <18F4550.h>
#Fuses xt,nowdt,noprotect,cpudiv1
#Use Delay (Clock= 4 MHz)
#define LCD_ENABLE_PIN PIN_D2
#define LCD_RS_PIN PIN_D0
#define LCD_RW_PIN PIN_D1
#define LCD_DATA4 PIN_D4
#define LCD_DATA5 PIN_D5
#define LCD_DATA6 PIN_D6
#define LCD_DATA7 PIN_D7
#include <lcd.c>

int32 t=1000;
int32 tp=5000;
int cont=1;
int actual=1;
int recorrer=0;
int tiempo=0,minuto=0;
boolean Start=true,Cro=true;

#Int_Ext
void Emergencia(){
   printf(lcd_putc,"EMERGENCIA \f");
   Start=false;
   Output_low(pin_E1);
   Output_low(pin_E0);
}
void puerta(){
   Output_low(pin_A1);
   Output_high(pin_A0);
   delay_ms(tp);
   Output_low(pin_A0);
   Output_low(pin_A1);
}
void Cronometro(){
  // delay_s(1);
   tiempo=tiempo+1;
   if (tiempo>60){
      minuto=1+minuto;      
   }
}
void der(recorrer){
   lcd_gotoxy(1,1);
   printf(lcd_putc,"subiendo");
   output_high(pin_E0);
   delay_ms(recorrer*t);
   Output_low(pin_E0);
   printf(lcd_putc,"\f");
}
void izq(recorrer){
   lcd_gotoxy(1,1);
   printf(lcd_putc,"bajando");
   Output_high(pin_E1);
   delay_ms(recorrer*t);
   output_low(pin_E1);
   printf(lcd_putc,"\f");
}
void main(){
   set_tris_A(0xff);
   set_tris_B(0xff);
   set_tris_C(0xff);
   set_tris_A(0x00);
   set_tris_A(0x00);
   lcd_Init();
   Enable_Interrupts(Int_Ext);
   Enable_Interrupts(Global);
   Ext_Int_Edge(0, L_TO_H);
   lcd_gotoxy(1,1);
   printf(lcd_putc,"Piso %i",cont);
   while(Start){
      if(input(pin_C0)==1){
         cont=1;
      }
      if(input(pin_C1)==1){
         cont=2;
      }
      if(input(pin_C2)==1){
         cont=3;
      }
      if(input(pin_C4)==1){
         cont=4;
      }
      while(cont>actual){
         recorrer=cont-actual;
         der(recorrer);
         lcd_gotoxy(1,1);
         printf(lcd_putc,"Piso %i",cont);
         puerta();
         actual=cont;
      }
      while(cont<actual){
         recorrer=-cont+actual;
         izq(recorrer);
         lcd_gotoxy(1,1);
         printf(lcd_putc,"piso %i",cont);
         puerta();
         actual=cont;         
      }
   }
}

