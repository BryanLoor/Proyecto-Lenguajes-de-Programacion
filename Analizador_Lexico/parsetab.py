
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ARRAY BREAK CADENA CASE CDER CIZQ CONSTANTE DIFERENTE DIVISION DO ELSE END ENTERO FOR FUNCION HASH IF IGUAL LDER LIZQ MAS MAYOR MENOR OR PDER PIZQ POTENCIA PROD PUTS RANGO RESTA UNLESS VARIABLE_CLASE VARIABLE_GLOBAL VARIABLE_LOCAL VARIABLE_OBJETO WHILEcodigo : algoritmo\n                | algoritmo codigo\n\n     algoritmo : asignacion\n                    | expresion\n                    | comparacion\n                    | sentenciaWHILE\n\n    sentenciaWHILE : WHILE  comparacion DO codigo END\n    asignacion : variables IGUAL expresion\n\n                    expresion : valor\n\n    expresion : valor operadorMat expresioncomparacion : expresion operadorComp expresionoperadorMat : MAS\n                | RESTA\n                | PROD\n                | DIVISION\n    operadorComp : MAYOR\n                | MENOR\n                | IGUAL\n                | DIFERENTE\n    valor : ENTERO\n                | variables\n     variables : VARIABLE_LOCAL\n                | VARIABLE_GLOBAL\n                | VARIABLE_OBJETO\n                | VARIABLE_CLASE\n                | CONSTANTE\n    '
    
_lr_action_items = {'WHILE':([0,2,3,4,5,6,7,8,10,11,12,13,14,15,30,31,32,33,34,36,],[9,9,-3,-4,-5,-6,-21,-9,-22,-23,-24,-25,-26,-20,-21,-11,-8,-10,9,-7,]),'VARIABLE_LOCAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,30,31,32,33,34,36,],[10,10,-3,-4,-5,-6,-21,-9,10,-22,-23,-24,-25,-26,-20,10,-16,-17,-18,-19,10,10,-12,-13,-14,-15,-21,-11,-8,-10,10,-7,]),'VARIABLE_GLOBAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,30,31,32,33,34,36,],[11,11,-3,-4,-5,-6,-21,-9,11,-22,-23,-24,-25,-26,-20,11,-16,-17,-18,-19,11,11,-12,-13,-14,-15,-21,-11,-8,-10,11,-7,]),'VARIABLE_OBJETO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,30,31,32,33,34,36,],[12,12,-3,-4,-5,-6,-21,-9,12,-22,-23,-24,-25,-26,-20,12,-16,-17,-18,-19,12,12,-12,-13,-14,-15,-21,-11,-8,-10,12,-7,]),'VARIABLE_CLASE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,30,31,32,33,34,36,],[13,13,-3,-4,-5,-6,-21,-9,13,-22,-23,-24,-25,-26,-20,13,-16,-17,-18,-19,13,13,-12,-13,-14,-15,-21,-11,-8,-10,13,-7,]),'CONSTANTE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,30,31,32,33,34,36,],[14,14,-3,-4,-5,-6,-21,-9,14,-22,-23,-24,-25,-26,-20,14,-16,-17,-18,-19,14,14,-12,-13,-14,-15,-21,-11,-8,-10,14,-7,]),'ENTERO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,30,31,32,33,34,36,],[15,15,-3,-4,-5,-6,-21,-9,15,-22,-23,-24,-25,-26,-20,15,-16,-17,-18,-19,15,15,-12,-13,-14,-15,-21,-11,-8,-10,15,-7,]),'$end':([1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,30,31,32,33,36,],[0,-1,-3,-4,-5,-6,-21,-9,-22,-23,-24,-25,-26,-20,-2,-21,-11,-8,-10,-7,]),'END':([2,3,4,5,6,7,8,10,11,12,13,14,15,16,30,31,32,33,35,36,],[-1,-3,-4,-5,-6,-21,-9,-22,-23,-24,-25,-26,-20,-2,-21,-11,-8,-10,36,-7,]),'MAYOR':([4,7,8,10,11,12,13,14,15,29,30,33,],[18,-21,-9,-22,-23,-24,-25,-26,-20,18,-21,-10,]),'MENOR':([4,7,8,10,11,12,13,14,15,29,30,33,],[19,-21,-9,-22,-23,-24,-25,-26,-20,19,-21,-10,]),'IGUAL':([4,7,8,10,11,12,13,14,15,29,30,33,],[20,22,-9,-22,-23,-24,-25,-26,-20,20,-21,-10,]),'DIFERENTE':([4,7,8,10,11,12,13,14,15,29,30,33,],[21,-21,-9,-22,-23,-24,-25,-26,-20,21,-21,-10,]),'MAS':([7,8,10,11,12,13,14,15,30,],[-21,24,-22,-23,-24,-25,-26,-20,-21,]),'RESTA':([7,8,10,11,12,13,14,15,30,],[-21,25,-22,-23,-24,-25,-26,-20,-21,]),'PROD':([7,8,10,11,12,13,14,15,30,],[-21,26,-22,-23,-24,-25,-26,-20,-21,]),'DIVISION':([7,8,10,11,12,13,14,15,30,],[-21,27,-22,-23,-24,-25,-26,-20,-21,]),'DO':([8,10,11,12,13,14,15,28,30,31,33,],[-9,-22,-23,-24,-25,-26,-20,34,-21,-11,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,2,34,],[1,16,35,]),'algoritmo':([0,2,34,],[2,2,2,]),'asignacion':([0,2,34,],[3,3,3,]),'expresion':([0,2,9,17,22,23,34,],[4,4,29,31,32,33,4,]),'comparacion':([0,2,9,34,],[5,5,28,5,]),'sentenciaWHILE':([0,2,34,],[6,6,6,]),'variables':([0,2,9,17,22,23,34,],[7,7,30,30,30,30,7,]),'valor':([0,2,9,17,22,23,34,],[8,8,8,8,8,8,8,]),'operadorComp':([4,29,],[17,17,]),'operadorMat':([8,],[23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> algoritmo','codigo',1,'p_codigo','sintactico_yacc.py',19),
  ('codigo -> algoritmo codigo','codigo',2,'p_codigo','sintactico_yacc.py',20),
  ('algoritmo -> asignacion','algoritmo',1,'p_algoritmo','sintactico_yacc.py',25),
  ('algoritmo -> expresion','algoritmo',1,'p_algoritmo','sintactico_yacc.py',26),
  ('algoritmo -> comparacion','algoritmo',1,'p_algoritmo','sintactico_yacc.py',27),
  ('algoritmo -> sentenciaWHILE','algoritmo',1,'p_algoritmo','sintactico_yacc.py',28),
  ('sentenciaWHILE -> WHILE comparacion DO codigo END','sentenciaWHILE',5,'p_sentenciaWhile','sintactico_yacc.py',33),
  ('asignacion -> variables IGUAL expresion','asignacion',3,'p_asignacion','sintactico_yacc.py',38),
  ('expresion -> valor','expresion',1,'p_expresion','sintactico_yacc.py',43),
  ('expresion -> valor operadorMat expresion','expresion',3,'p_expresion_aritmetica','sintactico_yacc.py',47),
  ('comparacion -> expresion operadorComp expresion','comparacion',3,'p_comparacion','sintactico_yacc.py',50),
  ('operadorMat -> MAS','operadorMat',1,'p_operadorMat','sintactico_yacc.py',53),
  ('operadorMat -> RESTA','operadorMat',1,'p_operadorMat','sintactico_yacc.py',54),
  ('operadorMat -> PROD','operadorMat',1,'p_operadorMat','sintactico_yacc.py',55),
  ('operadorMat -> DIVISION','operadorMat',1,'p_operadorMat','sintactico_yacc.py',56),
  ('operadorComp -> MAYOR','operadorComp',1,'p_operadorComp','sintactico_yacc.py',59),
  ('operadorComp -> MENOR','operadorComp',1,'p_operadorComp','sintactico_yacc.py',60),
  ('operadorComp -> IGUAL','operadorComp',1,'p_operadorComp','sintactico_yacc.py',61),
  ('operadorComp -> DIFERENTE','operadorComp',1,'p_operadorComp','sintactico_yacc.py',62),
  ('valor -> ENTERO','valor',1,'p_valor','sintactico_yacc.py',67),
  ('valor -> variables','valor',1,'p_valor','sintactico_yacc.py',68),
  ('variables -> VARIABLE_LOCAL','variables',1,'p_variables','sintactico_yacc.py',72),
  ('variables -> VARIABLE_GLOBAL','variables',1,'p_variables','sintactico_yacc.py',73),
  ('variables -> VARIABLE_OBJETO','variables',1,'p_variables','sintactico_yacc.py',74),
  ('variables -> VARIABLE_CLASE','variables',1,'p_variables','sintactico_yacc.py',75),
  ('variables -> CONSTANTE','variables',1,'p_variables','sintactico_yacc.py',76),
]