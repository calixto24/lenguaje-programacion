:- dynamic estudiante/11.

% estudiante(
%   Nombre,
%   Promedio,
%   Asistencia,
%   Ingreso,
%   Dependientes,
%   Trabaja,
%   Discapacidad,
%   Orfandad,
%   TipoColegio,
%   Zona,
%   Departamento
% ).

% DEPARTAMENTOS PRIORIZADOS ------------------------------

departamento_priorizado(ayacucho).
departamento_priorizado(apurimac).
departamento_priorizado(cajamarca).
departamento_priorizado(huancavelica).
departamento_priorizado(puno).

% REGLAS AUXILIARES ------------------------------

trabaja(Nombre):-
    estudiante(Nombre,_,_,_,_,si,_,_,_,_,_).

discapacitado(Nombre):-
    estudiante(Nombre,_,_,_,_,_,si,_,_,_,_).

huerfano(Nombre):-
    estudiante(Nombre,_,_,_,_,_,_,si,_,_,_).

colegio_publico(Nombre):-
    estudiante(Nombre,_,_,_,_,_,_,_,publico,_,_).

zona_rural(Nombre):-
    estudiante(Nombre,_,_,_,_,_,_,_,_,rural,_).

familia_numerosa(Nombre):-

    estudiante(
        Nombre,
        _,_,_,Dependientes,
        _,_,_,_,_,_
    ),

    Dependientes >= 4.

departamento_prioritario(Nombre):-

    estudiante(
        Nombre,
        _,_,_,_,_,_,_,_,_,
        Departamento
    ),

    departamento_priorizado(Departamento).

% MÉRITO ACADÉMICO ------------------------------

excelencia_academica(Nombre):-

    estudiante(
        Nombre,
        Promedio,
        Asistencia,
        _,_,_,_,_,_,_,_
    ),

    Promedio >= 18,
    Asistencia >= 90.

buen_rendimiento(Nombre):-

    estudiante(
        Nombre,
        Promedio,
        Asistencia,
        _,_,_,_,_,_,_,_
    ),

    Promedio >= 16,
    Asistencia >= 85.

rendimiento_aceptable(Nombre):-

    estudiante(
        Nombre,
        Promedio,
        Asistencia,
        _,_,_,_,_,_,_,_
    ),

    Promedio >= 15,
    Asistencia >= 85.

% NECESIDAD ECONÓMICA ------------------------------

alta_necesidad(Nombre):-

    estudiante(
        Nombre,
        _,_,
        Ingreso,
        _,_,_,_,_,_,_
    ),

    Ingreso =< 1200.

necesidad_media(Nombre):-

    estudiante(
        Nombre,
        _,_,
        Ingreso,
        _,_,_,_,_,_,_
    ),

    Ingreso =< 1800.

% PRIORIDAD SOCIAL ------------------------------

prioridad_social(Nombre):-

    discapacitado(Nombre).

prioridad_social(Nombre):-

    huerfano(Nombre).

% CONTEXTO SOCIOECONÓMICO ------------------------------

contexto_vulnerable(Nombre):-

    familia_numerosa(Nombre).

contexto_vulnerable(Nombre):-

    trabaja(Nombre).

contexto_vulnerable(Nombre):-

    colegio_publico(Nombre).

contexto_vulnerable(Nombre):-

    zona_rural(Nombre).

contexto_vulnerable(Nombre):-

    departamento_prioritario(Nombre).

% REGLAS DE BECAS ------------------------------

% BECA INTEGRAL (100%)

tipo_beca(Nombre,'Beca Integral (100%)'):-

    excelencia_academica(Nombre),

    alta_necesidad(Nombre),

    contexto_vulnerable(Nombre),

    !.

% BECA PARCIAL (70%)

tipo_beca(Nombre,'Beca Parcial (70%)'):-

    \+ tipo_beca(Nombre,'Beca Integral (100%)'),

    \+ tipo_beca(Nombre,'Beca de Apoyo Social (80%)'),

    buen_rendimiento(Nombre),

    necesidad_media(Nombre),

    (
        trabaja(Nombre)
        ;
        familia_numerosa(Nombre)
    ),

    !.

% BECA APOYO SOCIAL (80%)

tipo_beca(Nombre,'Beca de Apoyo Social (80%)'):-

    \+ tipo_beca(Nombre,'Beca Integral (100%)'),

    prioridad_social(Nombre),

    estudiante(
        Nombre,
        Promedio,
        Asistencia,
        _,_,_,_,_,_,_,_
    ),

    Promedio >= 14,
    Asistencia >= 80,

    !.

% BECA ESFUERZO ACADÉMICO (60%)

tipo_beca(Nombre,'Beca por Esfuerzo Académico (60%)'):-

    \+ tipo_beca(Nombre,'Beca Integral (100%)'),

    \+ tipo_beca(Nombre,'Beca de Apoyo Social (80%)'),

    \+ tipo_beca(Nombre,'Beca Parcial (70%)'),

    trabaja(Nombre),

    rendimiento_aceptable(Nombre),

    !.

% NO ELEGIBLE

tipo_beca(Nombre,'No Elegible'):-

    estudiante(
        Nombre,
        _,_,_,_,_,_,_,_,_,_
    ),

    \+ tipo_beca(Nombre,'Beca Integral (100%)'),

    \+ tipo_beca(Nombre,'Beca de Apoyo Social (80%)'),

    \+ tipo_beca(Nombre,'Beca Parcial (70%)'),

    \+ tipo_beca(Nombre,'Beca por Esfuerzo Académico (60%)').