 CREATE TABLE patient_details (
        Name  varchar(220) NOT NULL,
        Age   int NOT NULL,
        Address varchar(220),
        Doctor_recommended varchar(220),
 
);
CREATE TABLE doctor_details (
        name varchar(220) primary key,
        specialisation varchar(220),
        age int,
        address varchar(220),
        contact varchar(220),
        fees int,
        monthly_salary int,
        
 
);
CREATE TABLE nurse_details (
        name varchar(220) primary key,
        age int,
        address varchar(220),
        contact varchar(220),
        monthly_salary int,
        
 
);
CREATE TABLE other_workers_details (
        name varchar(220) primary key,
        age int,
        address varchar(220),
        contact varchar(220),
        monthly_salary int,
        
 
);
CREATE TABLE user_data (
        username varchar(220) primary key,
        password varchar(220) default'000',
);