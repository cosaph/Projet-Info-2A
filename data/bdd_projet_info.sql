DROP SCHEMA IF EXISTS projetInfo CASCADE;
CREATE SCHEMA projetInfo;

--------------------------------------------------------------
-- Critere
--------------------------------------------------------------

DROP TABLE IF EXISTS projetInfo.critere CASCADE;

CREATE TABLE projetInfo.critere (
    id_crit integer PRIMARY KEY,
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
    id_stage integer PRIMARY KEY,
    lien text,
    specialite text,
    code_insee text,
    date_debut text,
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
        
INSERT INTO projetInfo.critere(id_crit, code_insee_cible, specialite, duree_min, duree_max) values 
(12, '47001','blabla', 3, 4)
;
	
update projetinfo.utilisateur 
set 
mdp = 'gfgfg',
code_insee_residence = '13055', 
souhaite_alertes  = True,
stage_trouve =False, 
id_crit = 11
where email = 'bvbvbv@sdgdggd.com'
RETURNING email;

delete from projetinfo.utilisateur 
where email = 'bvbvbv@sdgdggd.com'
RETURNING email;


SELECT email
FROM projetinfo.utilisateur 
where email = 'gfgfggf'

