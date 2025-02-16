
* Link: https://help.sap.com/doc/abapdocu_750_index_htm/7.50/en-US/index.htm

* Comentario de toda la linea de codigo, solo se colocar el asterisco al inicio
" Comentario de toda la linea de codigo, solo se colocar el asterisco al inicio

"Cómo se crea una variable en ABAP

"DATA al inicio con el tipo que corresponda
data my_var type string value 'Mi variable'.

my_var = 'Nuevo valor'.

data(my_var_inline) = 'Variable en linea'.

"CONSTANTS
CONSTANTS my_constant type string value 'Constante'.

"Variable tipo entero
data my_int type i.
my_int = 10.

"Variable tipo decimal
data my_dec type p length 5 decimals 3.
my_dec = 56,789.

"Escribir en pantalla las variables
write:/ my_var.
write:/ my_var_inline.
write:/ my_int.
write:/ my_dec.