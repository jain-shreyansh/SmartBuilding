create table grocery
(
id integer primary key autoincrement,
want text,
apt_no integer not null,
my_name text
);

create table complaints
(
id integer primary key autoincrement,
apt_no integer not null,
my_name text,
complaint text
);