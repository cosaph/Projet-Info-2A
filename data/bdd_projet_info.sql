DROP SCHEMA IF EXISTS projetInfo CASCADE;
CREATE SCHEMA projetInfo;


--------------------------------------------------------------
-- Les utilisateurs
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.utilisateur CASCADE ;
CREATE TABLE projetInfo.utilisateur (
    email text PRIMARY KEY,
    mdp text,
    code_insee_residence text,
    souhaite_alertes boolean,
    stage_trouve boolean,
    profil text
);



--------------------------------------------------------------
-- Stage
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.stage CASCADE;

CREATE TABLE projetInfo.stage  (
    url_stage text PRIMARY KEY, 
    titre text,
    specialite text,
    ville text
);

       
 --------------------------------------------------------------
-- associationStageUser
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.association_stage_user CASCADE;

CREATE TABLE projetInfo.association_stage_user (
    titre text,
    url_stage text,
    email text,
    critere text,
    ville text,
    CONSTRAINT pk_asso6 PRIMARY KEY (url_stage,email),
    CONSTRAINT fk_asso7 FOREIGN KEY (email)
        REFERENCES projetInfo.utilisateur(email),
    CONSTRAINT fk_asso8 FOREIGN KEY (url_stage)
        REFERENCES projetInfo.stage(url_stage));
        
