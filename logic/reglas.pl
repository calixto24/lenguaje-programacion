:- dynamic estudiante/14.

% --- Distritos Priorizados ---

distrito_priorizado(ate).
distrito_priorizado(huaycan).
distrito_priorizado(el_agustino).
distrito_priorizado(san_juan_de_lurigancho).
distrito_priorizado(chosica).

% --- Reglas Auxiliares (Evaluadas por Codigo) ---

puede_postular(Codigo):-
    estudiante(Codigo,_,_,_,_,_,_,_,_,_,_,_,_,no).

trabaja(Codigo):-
    estudiante(Codigo,_,_,_,_,_,_,_,si,_,_,_,_,_).

vive_solo(Codigo):-
    estudiante(Codigo,_,_,_,_,_,_,_,_,_,si,_,_,_).

discapacitado(Codigo):-
    estudiante(Codigo,_,_,_,_,_,_,_,_,_,_,si,_,_).

huerfano(Codigo):-
    estudiante(Codigo,_,_,_,_,_,_,_,_,_,_,_,si,_).

familia_numerosa(Codigo):-
    estudiante(Codigo,_,_,_,_,_,_,Dependientes,_,_,_,_,_,_),
    Dependientes >= 4.

trabajo_intensivo(Codigo):-
    estudiante(Codigo,_,_,_,_,_,_,_,si,Horas,_,_,_,_),
    Horas >= 20.

distrito_prioritario(Codigo):-
    estudiante(Codigo,_,_,_,_,Distrito,_,_,_,_,_,_,_,_),
    distrito_priorizado(Distrito).

% --- Reglas de Asignación de Becas ---

% 1. Beca Socioeconómica (70%)
tipo_beca(Codigo, 'Beca Socioeconomica (70%)'):-
    puede_postular(Codigo),
    estudiante(Codigo, _, Promedio, Asistencia, Creditos, _, Ingreso, _, _, _, _, _, _, _),
    Promedio >= 14,
    Asistencia >= 80,
    Creditos >= 18,
    Ingreso =< 1500,
    (
        vive_solo(Codigo)
        ;
        familia_numerosa(Codigo)
        ;
        distrito_prioritario(Codigo)
    ),
    !.

% 2. Beca de Inclusión (40%)
tipo_beca(Codigo, 'Beca de Inclusion (40%)'):-
    puede_postular(Codigo),
    \+ tipo_beca(Codigo, 'Beca Socioeconomica (70%)'),
    estudiante(Codigo, _, Promedio, Asistencia, Creditos, _, _, _, _, _, _, _, _, _),
    Promedio >= 13,
    Asistencia >= 80,
    Creditos >= 18,
    (
        discapacitado(Codigo)
        ;
        huerfano(Codigo)
    ),
    !.

% 3. Beca por Esfuerzo Academico (20%)
tipo_beca(Codigo, 'Beca por Esfuerzo Academico (20%)'):-
    puede_postular(Codigo),
    \+ tipo_beca(Codigo, 'Beca Socioeconomica (70%)'),
    \+ tipo_beca(Codigo, 'Beca de Inclusion (40%)'),
    estudiante(Codigo, _, Promedio, Asistencia, Creditos, _, _, _, _, _, _, _, _, _),
    Promedio >= 15,
    Asistencia >= 85,
    Creditos >= 18,
    trabajo_intensivo(Codigo),
    !.

% 4. No Elegible
tipo_beca(Codigo, 'No Elegible'):-
    estudiante(Codigo,_,_,_,_,_,_,_,_,_,_,_,_,_),
    (
        \+ puede_postular(Codigo)
        ;
        (
            \+ tipo_beca(Codigo, 'Beca Socioeconomica (70%)'),
            \+ tipo_beca(Codigo, 'Beca de Inclusion (40%)'),
            \+ tipo_beca(Codigo, 'Beca por Esfuerzo Academico (20%)')
        )
    ).