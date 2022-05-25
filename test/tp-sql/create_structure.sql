CREATE DATABASE if not exists BDD_QCM_Projet;

USE BDD_QCM_Projet;

CREATE TABLE IF NOT EXISTS QCM (
    `id` INT(10) AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS question (
    `id` INT(10) AUTO_INCREMENT PRIMARY KEY,
    `intitule` VARCHAR(256) NOT NULL,  
    `rep_A` VARCHAR(256) NOT NULL,
    `rep_B` VARCHAR(256) NOT NULL, 
    `rep_C` VARCHAR(256) NOT NULL, 
    `rep_Correcte` VARCHAR(256) NOT NULL,  
    `QCM_id` INT(10)
);
