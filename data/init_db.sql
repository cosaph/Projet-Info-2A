DROP SCHEMA IF EXISTS projetInfo CASCADE;
CREATE SCHEMA projetInfo;

--------------------------------------------------------------
-- Les utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.utilisateur CASCADE ;
CREATE TABLE projetInfo.utilisateur (
    email text PRIMARY KEY,
    mdp text NOT NULL,
    code_insee_residence text,
    souhaite_alertes boolean,
    stage_trouve boolean
);


--------------------------------------------------------------
-- Critere
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.critere CASCADE;

CREATE TABLE projetInfo.critere (
    id_crit SERIAL PRIMARY KEY,
    code_insee_cible text,
    specialite text,
    duree_min integer,
    duree_max integer
    -- id_attack_type integer REFERENCES tp.attack_type(id_attack_type),
    -- power integer,
    -- accuracy integer,
    -- element text,
    -- attack_name text UNIQUE NOT NULL,
    -- attack_description text
);


--------------------------------------------------------------
-- Stage
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.stage CASCADE;

CREATE TABLE projetInfo.stage  (
    id_stage serial PRIMARY KEY,
    lien text,
    specialite text,
    code_insee text,
    date_debut text,
    email_employeur text
);


--------------------------------------------------------------
-- contactEmployeur
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.contactEmployeur CASCADE;

CREATE TABLE projetInfo.contactEmployeur (
    email text PRIMARY KEY,
    prenom text,
    nom text,
    tel text,
);

--------------------------------------------------------------
-- associationCitereStage
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.associationCitereStage CASCADE;

CREATE TABLE projetInfo.associationCitereStage (
    id_crit text,
    id_stage text,
    CONSTRAINT pk_asso PRIMARY KEY (id_crit,id_stage)
);




---- Exemple

-- DROP TABLE IF EXISTS projetInfo.contactEmployeur CASCADE;

-- CREATE TABLE tp.pokemon (
--     id_pokemon_type integer REFERENCES tp.pokemon_type(id_pokemon_type),
--     name text UNIQUE NOT NULL,
--     id_pokemon serial PRIMARY KEY,
--     level integer,
--     hp integer,
--     attack integer,
--     defense integer,
--     spe_atk integer,
--     spe_def integer,
--     speed integer,
--     url_image text
-- );

-- -- Comme on va creer des pokemon en forcant les id_pokemon
-- -- il faut maj a la main la valeur de la sequence de la PK
-- ALTER SEQUENCE tp.pokemon_id_pokemon_seq RESTART WITH 899;


-- --------------------------------------------------------------
-- -- Attaques des Pokemons
-- --------------------------------------------------------------

-- DROP TABLE IF EXISTS tp.pokemon_attack CASCADE;

-- CREATE TABLE tp.pokemon_attack (
--     id_pokemon integer REFERENCES tp.pokemon(id_pokemon) ON DELETE CASCADE,
--     id_attack integer REFERENCES tp.attack(id_attack) ON DELETE CASCADE,
--     level integer,
--     PRIMARY KEY (id_pokemon, id_attack)
-- );