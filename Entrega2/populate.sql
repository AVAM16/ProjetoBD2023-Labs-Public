insert into customer values (1, 'Artur', 'artur@gmail.com', 111111111, 'Lagoaca');
insert into customer values (2, 'Francisco', 'francisco@gmail.com', 222222222, 'Angustias');
insert into customer values (3, 'Duarte', 'duarte@gmail.com', 333333333, 'Orelhudo');
insert into customer values (4, 'Joao', 'jo@gmail.com', 444444444, 'Cabeceiras');

insert into eorder values (1, '2023-01-22 00:01');
insert into eorder values (2, '2023-01-12 10:05');
insert into eorder values (3, '2022-05-23 00:25');
insert into eorder values (4, '2023-01-01 05:01');
insert into eorder values (5, '2023-06-24 19:01');

insert into sale values (1);
insert into sale values (2);
insert into sale values (3);
insert into sale values (4);

insert into employee values (111111111, 111111111, '2000-01-01', 'Alberto');
insert into employee values (222222222, 222222222, '2001-02-02', 'Joaquim');
insert into employee values (333333333, 333333333, '1999-07-02', 'Ze');

insert into department values ('Vendas');
insert into department values ('Manutencao Site');
insert into department values ('Recursos Humanos');
insert into department values ('Apoio ao Cliente');

insert into workplace values ('Lisboa', 8.5207, 26.6134);
insert into workplace values ('Porto', 88.9328, 162.8080);
insert into workplace values ('Algarve', 41.9139, -19.9400);

insert into office values ('Lisboa');

insert into warehouse values ('Lisboa');
insert into warehouse values ('Porto');

insert into product values (1, 'PS5', 'Consola de Jogos', 499.99);
insert into product values (2, 'XBox', 'Consola de Jogos', 479.99);
insert into product values (3, 'Apple IPhone 17', 'Telemovel', 2299.99);
insert into product values (4, 'Samsung S43', 'Telemovel', 1799.99);
insert into product values (5, 'Google Chromecast', 'Tv Box', 69.99);
insert into product values (6, 'Carregador 33W USB-C', 'Carregador', 39.99);

insert into ean_product values (1, 111111111);
insert into ean_product values (2, 222222222);
insert into ean_product values (5, 333333333);

insert into supplier values (1, 'Porto', 'QuimTech', 1, '2023-01-01');
insert into supplier values (2, 'Branganca', 'Los Tech Hermanos', 2, '2023-01-01');
insert into supplier values (3, 'Lisboa', 'Big Tech', 3, '2022-01-01');
insert into supplier values (4, 'Beja', 'The Top Tech', 4, '2023-01-01');
insert into supplier values (5, 'Torres Vedras', 'iGus', 5, '2020-01-01');
insert into supplier values (6, 'Freixo de Espada a Cinta', 'Nikocado Tech', 6, '2018-01-01');
insert into supplier values (7, 'Braga', 'Walther Tech', 6, '2018-04-01');

insert into process values (111111111, 1);
insert into process values (222222222, 2);
insert into process values (333333333, 3);
insert into process values (333333333, 4);

insert into places values (1, 1);
insert into places values (2, 2);
insert into places values (3, 3);
insert into places values (4, 4);

insert into pay values (1,1);
insert into pay values (2,2);
insert into pay values (3,3);

insert into works values ('Lisboa', 111111111, 'Vendas');
insert into works values ('Porto', 222222222, 'Apoio ao Cliente');
insert into works values ('Porto', 333333333, 'Manutencao Site');

insert into contains values (1, 6, 1);
insert into contains values (2, 3, 1);
insert into contains values(3, 5, 5);
insert into contains values(4, 6, 5);

insert into delivery values ('Lisboa', 1);
insert into delivery values ('Porto', 3);
