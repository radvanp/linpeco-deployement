#!/bin/bash
#vytvorenie projektu
$django-admin startproject linpeco
#vytvorenie aplikacie
cd linpeco
$python3 manage.py startapp app
#vytvorenie tabuliek
$python3 manage.py migrate

#python3 manage.py migrate
#Operations to perform:
# Apply all migrations: admin, auth, contenttypes, sessions
#Running migrations:
#  Applying contenttypes.0001_initial... OK
#  Applying auth.0001_initial... OK
#  Applying admin.0001_initial... OK
#  Applying admin.0002_logentry_remove_auto_add... OK
#  Applying admin.0003_logentry_add_action_flag_choices... OK
#  Applying contenttypes.0002_remove_content_type_name... OK
#  Applying auth.0002_alter_permission_name_max_length... OK
#  Applying auth.0003_alter_user_email_max_length... OK
#  Applying auth.0004_alter_user_username_opts... OK
#  Applying auth.0005_alter_user_last_login_null... OK
#  Applying auth.0006_require_contenttypes_0002... OK
#  Applying auth.0007_alter_validators_add_error_messages... OK
#  Applying auth.0008_alter_user_username_max_length... OK
#  Applying auth.0009_alter_user_last_name_max_length... OK
#  Applying auth.0010_alter_group_name_max_length... OK
#  Applying auth.0011_update_proxy_permissions... OK
#  Applying auth.0012_alter_user_first_name_max_length... OK
#  Applying sessions.0001_initial... OK
$python3 manage.py makemigrations app
#oprava chyb ->maxlength->max_length v models.py
#doplnene -> on_delete=models.CASCADE,
$python3 manage.py makemigrations app
#Migrations for 'app':
#  app/migrations/0001_initial.py
#    - Create model Device
#    - Create model Place
#    - Create model RecordSumDay
#    - Create model RecordSumHour
#    - Create model RecordSumMonth
#    - Create model RecordSumYear
#    - Create model Record
#    - Add field place to device
#radvan@peterr:~/DJANGO/NOV/linpeco$
$python3 manage.py sqlmigrate app 0001
#vytvori tabulky a indexy*
#BEGIN;
#--
#-- Create model Device
#--
#CREATE TABLE "sg_device" ("device" integer NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "tms" timestamp with time zone NOT NULL);
#--
#-- Create model Place
#--
#CREATE TABLE "sg_place" ("place" integer NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "tms" timestamp with time zone NOT NULL);
#--
#-- Create model RecordSumDay
#--
#CREATE TABLE "sg_recordsumday" ("date" date NOT NULL PRIMARY KEY, "place" varchar(50) NOT NULL, "event_in" integer NOT NULL, "event_out" integer NOT NULL, "event_tag" integer NOT NULL);
#--
#-- Create model RecordSumHour
#--
#CREATE TABLE "sg_recordsumhour" ("date" timestamp with time zone NOT NULL PRIMARY KEY, "place" varchar(50) NOT NULL, "event_in" integer NOT NULL, "event_out" integer NOT NULL, "event_tag" integer NOT NULL);
#--
#-- Create model RecordSumMonth
#--
#CREATE TABLE "sg_recordsummonth" ("date" date NOT NULL PRIMARY KEY, "place" varchar(50) NOT NULL, "event_in" integer NOT NULL, "event_out" integer NOT NULL, "event_tag" integer NOT NULL);
#--
#-- Create model RecordSumYear
#--
#CREATE TABLE "sg_recordsumyear" ("date" date NOT NULL PRIMARY KEY, "place" varchar(50) NOT NULL, "event_in" integer NOT NULL, "event_out" integer NOT NULL, "event_tag" integer NOT NULL);
#--
#-- Create model Record
#--
#CREATE TABLE "sg_record" ("id" serial NOT NULL PRIMARY KEY, "event" integer NOT NULL, "tms" timestamp with time zone NOT NULL, "device" integer NOT NULL);
#--
#-- Add field place to device
#--
#ALTER TABLE "sg_device" ADD COLUMN "place" integer NOT NULL CONSTRAINT "sg_device_place_1ccdf2da_fk_sg_place_place" REFERENCES "sg_place"("place") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "sg_device_place_1ccdf2da_fk_sg_place_place" IMMEDIATE;
#ALTER TABLE "sg_record" ADD CONSTRAINT "sg_record_device_fb3da46f_fk_sg_device_device" FOREIGN KEY ("device") REFERENCES "sg_device" ("device") DEFERRABLE INITIALLY DEFERRED;
#CREATE INDEX "sg_record_device_fb3da46f" ON "sg_record" ("device");
#CREATE INDEX "sg_device_place_1ccdf2da" ON "sg_device" ("place");
#COMMIT;

$python3 manage.py migrate
#Operations to perform:
#  Apply all migrations: admin, app, auth, contenttypes, sessions
#Running migrations:
#  Applying app.0001_initial... OK

$python3 manage.py makemigrations
No changes detected

#Playing with the API
$python3 manage.py shell

#>>> from app.models import Place, Device
#>>> Place.objects.all()
#<QuerySet []>
#>>> Device.objects.all()
#<QuerySet []>

$python3 manage.py createsuperuser
#Používateľské meno (leave blank to use 'radvan'): radvan
#E-mailová adresa: peter.radvan@nov.sk
#Password:  789456123
#Password (again): 
#Toto heslo je používané príliš často.
#Toto heslo pozostáva iba z číslic.
#Bypass password validation and create user anyway? [y/N]: y
#Superuser created successfully.
$python manage.py runserver
#preklady
$python3 manage.py makemessages -a















