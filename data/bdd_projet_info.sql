DROP SCHEMA IF EXISTS projetInfo CASCADE;
CREATE SCHEMA projetInfo;

--------------------------------------------------------------
-- Critere
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.critere CASCADE;

CREATE TABLE projetInfo.critere (
    id_crit integer PRIMARY KEY,
    code_insee_cible text,
    rayon_km float,
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
    url_stage text PRIMARY KEY, 
    titre text,
    ville text,
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
    url_stage text,
    CONSTRAINT pk_asso PRIMARY KEY (id_crit,url_stage),
    CONSTRAINT fk_asso1 FOREIGN KEY (id_crit)
        REFERENCES projetInfo.critere(id_crit),
    CONSTRAINT fk_asso2 FOREIGN KEY (url_stage)
        REFERENCES projetInfo.stage(url_stage));
        
