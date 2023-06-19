START TRANSACTION;
SET CONSTRAINTS ALL DEFERRED;
insert into customer values (1, 'Artur', 'artur@gmail.com', 111111111, ' Kracc street 3828-308 Lagoaca');
insert into customer values (2, 'Francisco', 'francisco@gmail.com', 222222222, 'Grove Street 5555-765 Angustias');
insert into customer values (3, 'Duarte', 'duarte@gmail.com', 333333333, 'Negra Arroyo Lane 1111-456 Orelhudo');
insert into customer values (4, 'Joao', 'jo@gmail.com', 444444444, 'rua zezinho 1111-233 Cabeceiras');

insert into orders values (1, 1, '2023-01-22 00:01');
insert into orders values (2, 3, '2023-01-12 10:05');
insert into orders values (3, 4, '2022-05-23 00:25');
insert into orders values (4, 1, '2023-01-01 05:01');
insert into orders values (5, 2, '2023-06-24 19:01');
insert into orders values (6, 2, '2023-05-01 13:32');
insert into orders values (7, 3, '2023-02-02 10:05');
insert into orders values (8, 4, '2022-03-30 00:25');
insert into orders values (9, 1, '2023-01-01 05:01');
insert into orders values (10, 2, '2023-07-26 19:01');
insert into orders values (11, 1, '2023-08-03 13:32');
insert into orders values (12, 3, '2023-09-12 10:05');
insert into orders values (13, 4, '2022-10-23 00:25');
insert into orders values (14, 1, '2023-11-28 05:01');
insert into orders values (15, 2, '2023-12-27 19:01');
insert into orders values (16, 2, '2023-10-15 13:32');

insert into pay values (1,1);
insert into pay values (2,2);
insert into pay values (3,3);

insert into employee values (111111111, 111111111, '2000-01-01', 'Alberto');
insert into employee values (222222222, 222222222, '2001-02-02', 'Joaquim');
insert into employee values (333333333, 333333333, '1999-07-02', 'Ze');
insert into employee values (444444444, 444444444, '2010-05-12', 'Joaquim');

insert into process values (111111111, 1);
insert into process values (222222222, 2);
insert into process values (333333333, 3);
insert into process values (444444444, 4);
insert into process values (333333333, 8);
insert into process values (333333333, 13);

insert into department values ('Vendas');
insert into department values ('Manutencao Site');
insert into department values ('Recursos Humanos');
insert into department values ('Apoio ao Cliente');
insert into department values ('Armazem');

insert into workplace values ('avenida Eusebio da Silva Ferreira 3456-097 Lisboa', 8.5207, 26.6134);
insert into workplace values ('avenida Pinto da Costa 4564-243 Porto', 88.9328, 162.8080);
insert into workplace values ('rua da Falesia 1825-857 Algarve', 41.9139, -19.9400);


insert into warehouse values ('avenida Eusebio da Silva Ferreira 3456-097 Lisboa');
insert into warehouse values ('avenida Pinto da Costa 4564-243 Porto');
insert into warehouse values ('rua da Falesia 1825-857 Algarve');

insert into works values (111111111, 'Vendas','avenida Eusebio da Silva Ferreira 3456-097 Lisboa');
insert into works values (222222222, 'Apoio ao Cliente', 'avenida Pinto da Costa 4564-243 Porto');
insert into works values (333333333, 'Manutencao Site' , 'avenida Pinto da Costa 4564-243 Porto');
insert into works values (444444444, 'Armazem', 'rua da Falesia 1825-857 Algarve');

insert into product values (1, 'PS5', 'Consola de Jogos', 499.99);
insert into product values (2, 'XBox', 'Consola de Jogos', 479.99);
insert into product values (3, 'Apple IPhone 17', 'Telemovel', 2299.99);
insert into product values (4, 'Samsung S43', 'Telemovel', 1799.99);
insert into product values (5, 'Google Chromecast', 'Tv Box', 69.99);
insert into product values (6, 'Carregador 33W USB-C', 'Carregador', 39.99);

insert into contains values (1, 6, 1);
insert into contains values (2, 3, 1);
insert into contains values(3, 5, 5);
insert into contains values(4, 1, 5);
insert into contains values (5, 2, 2);
insert into contains values (6, 1, 3);
insert into contains values(7, 4, 4);
insert into contains values(8, 4, 4);
insert into contains values (9, 6, 10);
insert into contains values (10, 3, 5);
insert into contains values(11, 5, 2);
insert into contains values(12, 1, 3);
insert into contains values (13, 2, 4);
insert into contains values (14, 2, 4);
insert into contains values(15, 4, 1);
insert into contains values(16, 5, 1);

insert into supplier values (1, 'QuimTech','rua dos aliados 9876-354 Porto',  1, '2023-01-01');
insert into supplier values (2, 'Los Tech Hermanos', 'rua fixe 6666-666 Branganca',  2, '2023-01-01');
insert into supplier values (3, 'Big Tech', 'Bairro Alto 4567-654 Lisboa',  3, '2022-01-01');
insert into supplier values (4, 'The Top Tech', 'rua do Beijo 9203-246 Beja',  4, '2023-01-01');
insert into supplier values (5, 'iGus', 'rua do Xadrez 7777-010 Torres Vedras',  5, '2020-01-01');
insert into supplier values (6, 'Nikocado Tech', 'rua Las Vegas 3015-279 Freixo de Espada a Cinta',  6, '2018-01-01');
insert into supplier values (7, 'Walther Tech', 'rua Antonio Salvador 3584-233 Braga',  6, '2018-04-01');

insert into delivery values ('avenida Eusebio da Silva Ferreira 3456-097 Lisboa', 1);
insert into delivery values ('avenida Pinto da Costa 4564-243 Porto', 3);

COMMIT;
