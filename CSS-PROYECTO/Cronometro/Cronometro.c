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


