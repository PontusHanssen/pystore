insert into products (name,buy,sell,active) values("Bitburger", 14.90, 15, 1);
insert into products (name,buy,sell,active) values("Twisted", 18, 20, 1);

insert into accounts (name) values("Checkout");
insert into accounts (name) values("Vault");
insert into accounts (name) values("Sales");
insert into accounts (name) values("Purchases");

insert into locations (name) values("Cellar");
insert into locations (name) values("Store");

insert into transactions(datetime,name,from_id,to_id,balance) values(
    datetime('now'), "Purchase", 2, 4, 1018);
insert into transactions(datetime,name,from_id,to_id,balance) values(
    datetime('now'), "Sale", 3, 1, 32);

insert into stock (product,location,amount) values(1, 2, 19);
insert into stock (product,location,amount) values(2, 2, 19);
insert into stock (product,location,amount) values(1, 1, 20);
