
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ARRAY BEGINC BREAK CADENA CASE CDER CIZQ COMENTARIOL COMP_IGUAL CONSTANTE DIFERENTE DIVISION DO ELSE END ENDC ENTERO FOR FUNCION HASH IF IGUAL IN LDER LIZQ MAS MAYOR MENOR OR PDER PIZQ POTENCIA PROD PUTS RANGO RESTA UNLESS VARIABLE_CLASE VARIABLE_GLOBAL VARIABLE_LOCAL VARIABLE_OBJETO WHILEcodigo : algoritmo\n                | algoritmo codigo\n     algoritmo : asignacion\n                    | sentenciaWHILE\n                    | sentenciaFOR\n                    | puts\n                    | unless\n                    | comentarios\n                    | sentenciaIf\n     unless : UNLESS comparacion codigo END\n     sentenciaFOR : FOR variables IN range DO codigo END\n     range : ENTERO RANGO ENTERO\n     puts : PUTS CADENA\n    sentenciaWHILE : WHILE  comparacion DO codigo END\n    asignacion : variables IGUAL expresionexpresion : valor\n\n    expresion : valor operadorMat expresion\n                | PIZQ valor operadorMat expresion PDER\n\n\n    comparacion : expresion operadorComp expresion\n        | PIZQ expresion PDER operadorComp expresion\n    operadorMat : MAS\n                | RESTA\n                | PROD\n                | DIVISION\n                | POTENCIA\n    operadorComp : MAYOR\n                | MENOR\n                | COMP_IGUAL\n                | DIFERENTE\n    valor : ENTERO\n                | variables\n                | CADENA\n                | HASH\n                | ARRAY\n\n     variables : VARIABLE_LOCAL\n                | VARIABLE_GLOBAL\n                | VARIABLE_OBJETO\n                | VARIABLE_CLASE\n                | CONSTANTE\n    sentenciaIf : IF comparacion codigo END comentarios : COMENTARIOL\n\n\n    '
    
_lr_action_items = {'WHILE':([0,2,3,4,5,6,7,8,9,15,17,18,19,20,21,27,28,29,30,31,32,34,35,36,37,39,58,61,64,65,67,70,73,74,77,],[11,11,-3,-4,-5,-6,-7,-8,-9,-41,-35,-36,-37,-38,-39,-16,-30,-31,-32,-33,-34,-13,11,11,-15,11,-19,-17,-10,-40,-14,11,-20,-18,-11,]),'FOR':([0,2,3,4,5,6,7,8,9,15,17,18,19,20,21,27,28,29,30,31,32,34,35,36,37,39,58,61,64,65,67,70,73,74,77,],[12,12,-3,-4,-5,-6,-7,-8,-9,-41,-35,-36,-37,-38,-39,-16,-30,-31,-32,-33,-34,-13,12,12,-15,12,-19,-17,-10,-40,-14,12,-20,-18,-11,]),'PUTS':([0,2,3,4,5,6,7,8,9,15,17,18,19,20,21,27,28,29,30,31,32,34,35,36,37,39,58,61,64,65,67,70,73,74,77,],[13,13,-3,-4,-5,-6,-7,-8,-9,-41,-35,-36,-37,-38,-39,-16,-30,-31,-32,-33,-34,-13,13,13,-15,13,-19,-17,-10,-40,-14,13,-20,-18,-11,]),'UNLESS':([0,2,3,4,5,6,7,8,9,15,17,18,19,20,21,27,28,29,30,31,32,34,35,36,37,39,58,61,64,65,67,70,73,74,77,],[14,14,-3,-4,-5,-6,-7,-8,-9,-41,-35,-36,-37,-38,-39,-16,-30,-31,-32,-33,-34,-13,14,14,-15,14,-19,-17,-10,-40,-14,14,-20,-18,-11,]),'COMENTARIOL':([0,2,3,4,5,6,7,8,9,15,17,18,19,20,21,27,28,29,30,31,32,34,35,36,37,39,58,61,64,65,67,70,73,74,77,],[15,15,-3,-4,-5,-6,-7,-8,-9,-41,-35,-36,-37,-38,-39,-16,-30,-31,-32,-33,-34,-13,15,15,-15,15,-19,-17,-10,-40,-14,15,-20,-18,-11,]),'IF':([0,2,3,4,5,6,7,8,9,15,17,18,19,20,21,27,28,29,30,31,32,34,35,36,37,39,58,61,64,65,67,70,73,74,77,],[16,16,-3,-4,-5,-6,-7,-8,-9,-41,-35,-36,-37,-38,-39,-16,-30,-31,-32,-33,-34,-13,16,16,-15,16,-19,-17,-10,-40,-14,16,-20,-18,-11,]),'VARIABLE_LOCAL':([0,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,19,20,21,23,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,47,48,49,50,51,52,58,60,61,64,65,66,67,68,70,73,74,77,],[17,17,-3,-4,-5,-6,-7,-8,-9,17,17,17,-41,17,-35,-36,-37,-38,-39,17,17,-16,-30,-31,-32,-33,-34,-13,17,17,-15,17,17,17,-26,-27,-28,-29,17,-21,-22,-23,-24,-25,-19,17,-17,-10,-40,17,-14,17,17,-20,-18,-11,]),'VARIABLE_GLOBAL':([0,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,19,20,21,23,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,47,48,49,50,51,52,58,60,61,64,65,66,67,68,70,73,74,77,],[18,18,-3,-4,-5,-6,-7,-8,-9,18,18,18,-41,18,-35,-36,-37,-38,-39,18,18,-16,-30,-31,-32,-33,-34,-13,18,18,-15,18,18,18,-26,-27,-28,-29,18,-21,-22,-23,-24,-25,-19,18,-17,-10,-40,18,-14,18,18,-20,-18,-11,]),'VARIABLE_OBJETO':([0,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,19,20,21,23,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,47,48,49,50,51,52,58,60,61,64,65,66,67,68,70,73,74,77,],[19,19,-3,-4,-5,-6,-7,-8,-9,19,19,19,-41,19,-35,-36,-37,-38,-39,19,19,-16,-30,-31,-32,-33,-34,-13,19,19,-15,19,19,19,-26,-27,-28,-29,19,-21,-22,-23,-24,-25,-19,19,-17,-10,-40,19,-14,19,19,-20,-18,-11,]),'VARIABLE_CLASE':([0,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,19,20,21,23,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,47,48,49,50,51,52,58,60,61,64,65,66,67,68,70,73,74,77,],[20,20,-3,-4,-5,-6,-7,-8,-9,20,20,20,-41,20,-35,-36,-37,-38,-39,20,20,-16,-30,-31,-32,-33,-34,-13,20,20,-15,20,20,20,-26,-27,-28,-29,20,-21,-22,-23,-24,-25,-19,20,-17,-10,-40,20,-14,20,20,-20,-18,-11,]),'CONSTANTE':([0,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,19,20,21,23,26,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,47,48,49,50,51,52,58,60,61,64,65,66,67,68,70,73,74,77,],[21,21,-3,-4,-5,-6,-7,-8,-9,21,21,21,-41,21,-35,-36,-37,-38,-39,21,21,-16,-30,-31,-32,-33,-34,-13,21,21,-15,21,21,21,-26,-27,-28,-29,21,-21,-22,-23,-24,-25,-19,21,-17,-10,-40,21,-14,21,21,-20,-18,-11,]),'$end':([1,2,3,4,5,6,7,8,9,15,17,18,19,20,21,22,27,28,29,30,31,32,34,37,61,64,65,67,74,77,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-41,-35,-36,-37,-38,-39,-2,-16,-30,-31,-32,-33,-34,-13,-15,-17,-10,-40,-14,-18,-11,]),'END':([2,3,4,5,6,7,8,9,15,17,18,19,20,21,22,27,28,29,30,31,32,34,37,54,55,57,61,64,65,67,74,75,77,],[-1,-3,-4,-5,-6,-7,-8,-9,-41,-35,-36,-37,-38,-39,-2,-16,-30,-31,-32,-33,-34,-13,-15,64,65,67,-17,-10,-40,-14,-18,77,-11,]),'IGUAL':([10,17,18,19,20,21,],[23,-35,-36,-37,-38,-39,]),'PIZQ':([11,14,16,23,26,40,41,42,43,44,47,48,49,50,51,52,60,66,68,],[26,26,26,38,38,38,-26,-27,-28,-29,38,-21,-22,-23,-24,-25,38,38,38,]),'ENTERO':([11,14,16,23,26,38,40,41,42,43,44,47,48,49,50,51,52,53,60,66,68,71,],[28,28,28,28,28,28,28,-26,-27,-28,-29,28,-21,-22,-23,-24,-25,63,28,28,28,76,]),'CADENA':([11,13,14,16,23,26,38,40,41,42,43,44,47,48,49,50,51,52,60,66,68,],[30,34,30,30,30,30,30,30,-26,-27,-28,-29,30,-21,-22,-23,-24,-25,30,30,30,]),'HASH':([11,14,16,23,26,38,40,41,42,43,44,47,48,49,50,51,52,60,66,68,],[31,31,31,31,31,31,31,-26,-27,-28,-29,31,-21,-22,-23,-24,-25,31,31,31,]),'ARRAY':([11,14,16,23,26,38,40,41,42,43,44,47,48,49,50,51,52,60,66,68,],[32,32,32,32,32,32,32,-26,-27,-28,-29,32,-21,-22,-23,-24,-25,32,32,32,]),'MAS':([17,18,19,20,21,27,28,29,30,31,32,46,56,],[-35,-36,-37,-38,-39,48,-30,-31,-32,-33,-34,48,48,]),'RESTA':([17,18,19,20,21,27,28,29,30,31,32,46,56,],[-35,-36,-37,-38,-39,49,-30,-31,-32,-33,-34,49,49,]),'PROD':([17,18,19,20,21,27,28,29,30,31,32,46,56,],[-35,-36,-37,-38,-39,50,-30,-31,-32,-33,-34,50,50,]),'DIVISION':([17,18,19,20,21,27,28,29,30,31,32,46,56,],[-35,-36,-37,-38,-39,51,-30,-31,-32,-33,-34,51,51,]),'POTENCIA':([17,18,19,20,21,27,28,29,30,31,32,46,56,],[-35,-36,-37,-38,-39,52,-30,-31,-32,-33,-34,52,52,]),'MAYOR':([17,18,19,20,21,25,27,28,29,30,31,32,59,61,74,],[-35,-36,-37,-38,-39,41,-16,-30,-31,-32,-33,-34,41,-17,-18,]),'MENOR':([17,18,19,20,21,25,27,28,29,30,31,32,59,61,74,],[-35,-36,-37,-38,-39,42,-16,-30,-31,-32,-33,-34,42,-17,-18,]),'COMP_IGUAL':([17,18,19,20,21,25,27,28,29,30,31,32,59,61,74,],[-35,-36,-37,-38,-39,43,-16,-30,-31,-32,-33,-34,43,-17,-18,]),'DIFERENTE':([17,18,19,20,21,25,27,28,29,30,31,32,59,61,74,],[-35,-36,-37,-38,-39,44,-16,-30,-31,-32,-33,-34,44,-17,-18,]),'IN':([17,18,19,20,21,33,],[-35,-36,-37,-38,-39,53,]),'PDER':([17,18,19,20,21,27,28,29,30,31,32,45,46,61,69,72,74,],[-35,-36,-37,-38,-39,-16,-30,-31,-32,-33,-34,59,-16,-17,74,74,-18,]),'DO':([17,18,19,20,21,24,27,28,29,30,31,32,58,61,62,73,74,76,],[-35,-36,-37,-38,-39,39,-16,-30,-31,-32,-33,-34,-19,-17,70,-20,-18,-12,]),'RANGO':([63,],[71,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'codigo':([0,2,35,36,39,70,],[1,22,54,55,57,75,]),'algoritmo':([0,2,35,36,39,70,],[2,2,2,2,2,2,]),'asignacion':([0,2,35,36,39,70,],[3,3,3,3,3,3,]),'sentenciaWHILE':([0,2,35,36,39,70,],[4,4,4,4,4,4,]),'sentenciaFOR':([0,2,35,36,39,70,],[5,5,5,5,5,5,]),'puts':([0,2,35,36,39,70,],[6,6,6,6,6,6,]),'unless':([0,2,35,36,39,70,],[7,7,7,7,7,7,]),'comentarios':([0,2,35,36,39,70,],[8,8,8,8,8,8,]),'sentenciaIf':([0,2,35,36,39,70,],[9,9,9,9,9,9,]),'variables':([0,2,11,12,14,16,23,26,35,36,38,39,40,47,60,66,68,70,],[10,10,29,33,29,29,29,29,10,10,29,10,29,29,29,29,29,10,]),'comparacion':([11,14,16,],[24,35,36,]),'expresion':([11,14,16,23,26,40,47,60,66,68,],[25,25,25,37,45,58,61,69,72,73,]),'valor':([11,14,16,23,26,38,40,47,60,66,68,],[27,27,27,27,46,56,27,27,27,27,27,]),'operadorComp':([25,59,],[40,68,]),'operadorMat':([27,46,56,],[47,60,66,]),'range':([53,],[62,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> codigo","S'",1,None,None,None),
  ('codigo -> algoritmo','codigo',1,'p_codigo','sintactico_yacc.py',30),
  ('codigo -> algoritmo codigo','codigo',2,'p_codigo','sintactico_yacc.py',31),
  ('algoritmo -> asignacion','algoritmo',1,'p_algoritmo','sintactico_yacc.py',34),
  ('algoritmo -> sentenciaWHILE','algoritmo',1,'p_algoritmo','sintactico_yacc.py',35),
  ('algoritmo -> sentenciaFOR','algoritmo',1,'p_algoritmo','sintactico_yacc.py',36),
  ('algoritmo -> puts','algoritmo',1,'p_algoritmo','sintactico_yacc.py',37),
  ('algoritmo -> unless','algoritmo',1,'p_algoritmo','sintactico_yacc.py',38),
  ('algoritmo -> comentarios','algoritmo',1,'p_algoritmo','sintactico_yacc.py',39),
  ('algoritmo -> sentenciaIf','algoritmo',1,'p_algoritmo','sintactico_yacc.py',40),
  ('unless -> UNLESS comparacion codigo END','unless',4,'p_unless','sintactico_yacc.py',44),
  ('sentenciaFOR -> FOR variables IN range DO codigo END','sentenciaFOR',7,'p_sentenciaFor','sintactico_yacc.py',47),
  ('range -> ENTERO RANGO ENTERO','range',3,'p_range','sintactico_yacc.py',51),
  ('puts -> PUTS CADENA','puts',2,'p_puts','sintactico_yacc.py',55),
  ('sentenciaWHILE -> WHILE comparacion DO codigo END','sentenciaWHILE',5,'p_sentenciaWhile','sintactico_yacc.py',60),
  ('asignacion -> variables IGUAL expresion','asignacion',3,'p_asignacion','sintactico_yacc.py',64),
  ('expresion -> valor','expresion',1,'p_expresion','sintactico_yacc.py',67),
  ('expresion -> valor operadorMat expresion','expresion',3,'p_expresion_aritmetica','sintactico_yacc.py',72),
  ('expresion -> PIZQ valor operadorMat expresion PDER','expresion',5,'p_expresion_aritmetica','sintactico_yacc.py',73),
  ('comparacion -> expresion operadorComp expresion','comparacion',3,'p_comparacion','sintactico_yacc.py',79),
  ('comparacion -> PIZQ expresion PDER operadorComp expresion','comparacion',5,'p_comparacion','sintactico_yacc.py',80),
  ('operadorMat -> MAS','operadorMat',1,'p_operadorMat','sintactico_yacc.py',85),
  ('operadorMat -> RESTA','operadorMat',1,'p_operadorMat','sintactico_yacc.py',86),
  ('operadorMat -> PROD','operadorMat',1,'p_operadorMat','sintactico_yacc.py',87),
  ('operadorMat -> DIVISION','operadorMat',1,'p_operadorMat','sintactico_yacc.py',88),
  ('operadorMat -> POTENCIA','operadorMat',1,'p_operadorMat','sintactico_yacc.py',89),
  ('operadorComp -> MAYOR','operadorComp',1,'p_operadorComp','sintactico_yacc.py',92),
  ('operadorComp -> MENOR','operadorComp',1,'p_operadorComp','sintactico_yacc.py',93),
  ('operadorComp -> COMP_IGUAL','operadorComp',1,'p_operadorComp','sintactico_yacc.py',94),
  ('operadorComp -> DIFERENTE','operadorComp',1,'p_operadorComp','sintactico_yacc.py',95),
  ('valor -> ENTERO','valor',1,'p_valor','sintactico_yacc.py',100),
  ('valor -> variables','valor',1,'p_valor','sintactico_yacc.py',101),
  ('valor -> CADENA','valor',1,'p_valor','sintactico_yacc.py',102),
  ('valor -> HASH','valor',1,'p_valor','sintactico_yacc.py',103),
  ('valor -> ARRAY','valor',1,'p_valor','sintactico_yacc.py',104),
  ('variables -> VARIABLE_LOCAL','variables',1,'p_variables','sintactico_yacc.py',109),
  ('variables -> VARIABLE_GLOBAL','variables',1,'p_variables','sintactico_yacc.py',110),
  ('variables -> VARIABLE_OBJETO','variables',1,'p_variables','sintactico_yacc.py',111),
  ('variables -> VARIABLE_CLASE','variables',1,'p_variables','sintactico_yacc.py',112),
  ('variables -> CONSTANTE','variables',1,'p_variables','sintactico_yacc.py',113),
  ('sentenciaIf -> IF comparacion codigo END','sentenciaIf',4,'p_sentenciaIf','sintactico_yacc.py',116),
  ('comentarios -> COMENTARIOL','comentarios',1,'p_comentarios','sintactico_yacc.py',119),
]
