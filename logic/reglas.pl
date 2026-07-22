:- dynamic estudiante/3.

% estudiante(Nombre, Promedio, Asistencia).

% Reglas de inferencia

aprobado(Nombre):-
    estudiante(Nombre,Promedio,_),
    Promedio >= 11.


desaprobado(Nombre):-
    estudiante(Nombre,Promedio,_),
    Promedio < 11.


destacado(Nombre):-
    estudiante(Nombre,Promedio,Asistencia),
    Promedio >= 17,
    Asistencia >= 90.


candidato_beca(Nombre):-
    estudiante(Nombre,Promedio,Asistencia),
    Promedio >= 18,
    Asistencia >= 95.


requiere_tutoria(Nombre):-
    estudiante(Nombre,Promedio,_),
    Promedio < 13.


riesgo_desercion(Nombre):-
    estudiante(Nombre,Promedio,Asistencia),
    Promedio < 11,
    Asistencia < 70.


asistencia_critica(Nombre):-
    estudiante(Nombre,_,Asistencia),
    Asistencia < 70.


buen_rendimiento(Nombre):-
    estudiante(Nombre,Promedio,_),
    Promedio >= 15,
    Promedio <17.


rendimiento_regular(Nombre):-
    estudiante(Nombre,Promedio,_),
    Promedio >=11,
    Promedio <15.