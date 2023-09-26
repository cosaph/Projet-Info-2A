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

