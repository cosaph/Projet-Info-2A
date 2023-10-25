DROP SCHEMA IF EXISTS projetInfo CASCADE;
CREATE SCHEMA projetInfo;

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
);

--------------------------------------------------------------
-- Les utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.utilisateur CASCADE ;
CREATE TABLE projetInfo.utilisateur (
    email text PRIMARY KEY,
    mdp text NOT NULL,
    code_insee_residence text,
    souhaite_alertes boolean,
    stage_trouve boolean,
    id_crit integer REFERENCES projetInfo.critere(id_crit)
);


--------------------------------------------------------------
-- contactEmployeur
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.contact_employeur CASCADE;

CREATE TABLE projetInfo.contact_employeur (
    email text PRIMARY KEY,
    prenom text,
    nom text,
    tel text
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
    date_fin text,
    email_employeur text REFERENCES projetInfo.contact_employeur(email)
);



--------------------------------------------------------------
-- associationCitereStage
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.association_critere_stage CASCADE;

CREATE TABLE projetInfo.association_critere_stage (
    id_crit integer,
    id_stage integer,
    CONSTRAINT pk_asso PRIMARY KEY (id_crit,id_stage),
    CONSTRAINT fk_asso1 FOREIGN KEY (id_crit)
        REFERENCES projetInfo.critere(id_crit),
    CONSTRAINT fk_asso2 FOREIGN KEY (id_stage)
        REFERENCES projetInfo.stage(id_stage));



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