#-*- coding: utf-8-unix; -*-
from peewee import *

db = SqliteDatabase(None)

def init(path):
    db.init(path)

def open():
    db.connect()

def create_tables():
    db.create_tables([TipoEntrada, Entrada])

def close():
    db.close()

class BaseModel(Model):
    id = PrimaryKeyField()
    class Meta:
        database = db

class TipoEntrada(BaseModel):
    nome = CharField()

class Entrada(BaseModel):
    autor = CharField(index = True)
    titulo = CharField()
    ano = IntegerField()
    chave = CharField()
    bibtex = TextField(null = True)
    tipo_entrada = ForeignKeyField(TipoEntrada)
