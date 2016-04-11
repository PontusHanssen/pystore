drop table if exists products;
create table products(
	id integer primary key autoincrement,
	name text not null,
	buy real,
	sell real,
    active boolean
);

drop table if exists accounts;
create table accounts(
    id integer primary key autoincrement,
    name text not null
);

drop table if exists locations;
create table locations(
    id integer primary key autoincrement,
    name text not null
);


drop table if exists transactions;
create table transactions(
	id integer primary key autoincrement,
	datetime text not null,
	name text not null,
    from_id integer,
    to_id integer,
	balance real,
    foreign key(from_id) references accounts(id),
    foreign key(to_id) references accounts(id)
);

drop table if exists stock;
create table stock(
    product integer,
    location integer,
    amount, integer,
    foreign key(product) references products(id),
    foreign key(location) references locations(id)
);
