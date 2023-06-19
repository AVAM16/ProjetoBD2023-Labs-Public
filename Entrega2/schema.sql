drop table if exists Customer cascade;
drop table if exists eOrder cascade;
drop table if exists Sale cascade;
drop table if exists Employee cascade;
drop table if exists Department cascade;
drop table if exists Workplace cascade;
drop table if exists Office cascade;
drop table if exists Warehouse cascade;
drop table if exists Product cascade;
drop table if exists EAN_Product cascade;
drop table if exists Supplier cascade;
drop table if exists process cascade;
drop table if exists places cascade;
drop table if exists pay cascade;
drop table if exists works cascade;
drop table if exists contains cascade;
drop table if exists delivery cascade;

create table Customer(
    cust_no numeric(15) not null,
    name varchar(100) not null,
    email varchar(100) not null,
    phone numeric(12) not null,
    adress varchar(150) not null,
    primary key(cust_no),
    unique(email)
);

create table eOrder(
    order_no numeric(15) not null,
    date timestamp not null,
    primary key(order_no)
    --IC-6:Every Order (order_no) must exit in the table 'contains'
);

create table Sale(
    order_no numeric(15) not null,
    primary key(order_no),
    foreign key(order_no) references eOrder(order_no)
);

create table Employee(
    ssn numeric(11) not null,
    TIN numeric(9) not null,
    bdate date not null,
    name varchar(100) not null,
    primary key(ssn),
    unique(TIN)
    --IC-5:Every Employee (ssn) must exist in the table 'works'
);

create table Department(
    name varchar(100) not null,
    primary key(name)
);

create table Workplace(
    address char(150) not null,
    lat numeric(7,5) not null,
    long numeric(8,5) not null,
    primary key(address),
    check(lat <= 90 and lat >= -90),
    check(long <= 180 and long >= -180),
    unique(lat, long)
);

create table Office(
    address varchar(150) not null,
    primary key(address),
    foreign key(address) references Workplace(address)
);

create table Warehouse(
    address varchar(150) not null,
    primary key(address),
    foreign key(address) references Workplace(address)
);

create table Product(
    sku numeric(15) not null,
    name varchar(100) not null,
    description varchar(500) not null,
    price numeric(7,2) not null,
    primary key(sku)
    --IC-7:Every Product (sku) must exist in the table supply-contract
);

create table EAN_Product(
    sku numeric(15) not null,
    ean numeric(20) not null,
    primary key(sku),
    foreign key(sku) references Product(sku)
);

create table Supplier(
    TIN numeric(9) not null,
    address varchar(150) not null,
    name varchar(100) not null,
    sku numeric(15) not null,
    contractdate date not null,
    primary key(TIN),
    foreign key(sku) references Product(sku)
);

create table process(
    ssn numeric(11) not null,
    order_no numeric(15) not null,
    primary key(ssn, order_no),
    foreign key(ssn) references Employee(ssn),
    foreign key(order_no) references eOrder(order_no)
);

create table places(
    cust_no numeric(15) not null,
    order_no numeric(15) not null,
    primary key (cust_no, order_no),
    foreign key (cust_no) references Customer(cust_no),
    foreign key (order_no) references eOrder(order_no)
);

create table pay(
    cust_no numeric(15) not null,
    order_no numeric(15) not null,
    primary key (cust_no, order_no),
    foreign key (cust_no) references Customer(cust_no),
    foreign key (order_no) references Sale(order_no)
    --(IC-1) Customers can only pay for the Sale of an Order they have placed themselves
);

create table works(
    address char(150) not null,
    ssn numeric(11) not null,
    name varchar(100) not null,
    primary key (address, ssn, name),
    foreign key (address) references Workplace(address),
    foreign key (ssn) references Employee(ssn),
    foreign key (name) references Department(name)
);

create table contains(
    order_no numeric(15) not null,
    sku numeric(15) not null,
    qty numeric(3) not null,
    primary key (order_no, sku),
    foreign key (order_no) references eOrder(order_no),
    foreign key (sku) references Product(sku)
);

create table delivery(
    address varchar(150) not null,
    TIN numeric(9) not null,
    primary key (address,TIN),
    foreign key (address) references Warehouse(address),
    foreign key (TIN) references Supplier(TIN)
);