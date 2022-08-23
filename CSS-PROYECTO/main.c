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

unsigned int16 analogo;

int32 t=1000;
int32 tp=5000;
int cont=1;
int16 iterador=0;
int actual=1;
int recorrer=0,minutoR=0,segundoR=0;
int tiempo=0,minuto=0;
boolean Start=true,Cro=false;

#int_RB
void rb_isr(){
   if (input(pin_c4)==1){
      set_pwm1_duty(analogo);
   }
   if (input(pin_c5)==1){
      set_pwm1_duty(analogo);
   }   
   if(input(pin_C4)==0){
      if(input(pin_B4)==0){
         output_low(PIN_B4);
         output_low(PIN_B5);
         output_low(PIN_C4);
         output_low(PIN_C5);
         setup_ccp1(ccp_off);
         setup_ccp2(ccp_off);
         output_low(PIN_C1);
         output_low(PIN_C2);
         delay_ms(10);
         setup_ccp1(ccp_pwm);
         output_high(PIN_C4);
      }
   }
   if(input(pin_C5)==0){
      if(input(pin_B5)==0){
            output_low(PIN_B4);
            output_low(PIN_B5);
            output_low(PIN_C4);
            output_low(PIN_C5);
            setup_ccp1(ccp_off);
            setup_ccp2(ccp_off);
            output_low(PIN_C1);
            output_low(PIN_C2);
            delay_ms(10);
            setup_ccp2(ccp_pwm);
            output_high(PIN_C4);
            output_low(PIN_C5);
         }
      }
      else{
         output_low(PIN_B4);
            setup_ccp1(ccp_off);
            setup_ccp2(ccp_off); 
            output_low(PIN_B4);
            output_low(PIN_B5);
            output_low(PIN_C4);
            output_low(PIN_C5);
            output_low(PIN_C1);
            output_low(PIN_C2);
      }    
   }
   

void Configuracion(){
   setup_adc(ADC_CLOCK_DIV_32);
   setup_adc_ports(AN0);
   set_adc_channel(0);
   setup_timer_2(T2_DIV_BY_16,127,1);
   delay_ms(500);
}

void Cronometro(){
   if(Cro==true){
      tiempo++;
      if (tiempo>60){
      minuto++;
      }
   }else{
      minutoR=minuto+minutoR;
      segundoR=tiempo+segundoR;
      tiempo=0;
      minuto=0;
   }
}

#int_timer0
void timer0(){
   output_toggle(PIN_E2);
   Cronometro();
   lcd_gotoxy(1,2);
   printf(lcd_putc,"%2u : %2u",minutoR,segundoR);
   lcd_gotoxy(1,1);
   set_timer0(57724);
}


#Int_Ext
void Emergencia(){
   lcd_gotoxy(1,1);
   printf(lcd_putc,"EMERGENCIA");
   Start=false;
   Output_low(pin_E1);
   Output_low(pin_E0);
}
void puerta(){
   Output_low(pin_E7);
   Output_high(pin_B6);
   delay_ms(tp);
   Output_low(pin_B6);
   Output_high(pin_B7);
   delay_ms(tp);
   Output_low(pin_B7);
   Cro=false;
}
void der(recorrer){
   lcd_gotoxy(9,1);
   printf(lcd_putc,"subiendo");
   output_high(pin_C1);
   delay_ms(recorrer*t);
   Output_low(pin_C2);
   printf(lcd_putc,"\f");
}
void izq(recorrer){
   lcd_gotoxy(9,1);
   printf(lcd_putc,"bajando");
   Output_high(pin_C1);
   delay_ms(recorrer*t);
   output_low(pin_C2);
   printf(lcd_putc,"\f");
}
void main(){
   set_tris_A(0xff);
   set_tris_B(0xff);
   set_tris_C(0x00);
   set_tris_D(0x00);
   set_tris_E(0x00);
   lcd_Init();
   setup_timer_0(RTCC_INTERNAL | T0_DIV_256 );
   set_timer0(57724);
   Enable_Interrupts(Int_TIMER0);
   Enable_Interrupts(Int_Ext);
   Enable_Interrupts(Global);
   Enable_Interrupts(Int_RB);
   Ext_Int_Edge(0, L_TO_H);
   lcd_gotoxy(1,1);
   printf(lcd_putc,"Piso %i",cont);
   Configuracion();
   while(Start){
   analogo=read_adc();
      if(input(pin_A2)==1){
         Cro=true;
         cont=1;
      }
      if(input(pin_A3)==1){
         Cro=true;
         cont=2;
      }
      if(input(pin_A4)==1){
         Cro=true;
         cont=3;
      }
      if(input(pin_A5)==1){
         Cro=true;
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
         printf(lcd_putc,"Piso %i",cont);
         puerta();
         actual=cont;         
      }
   }
}
