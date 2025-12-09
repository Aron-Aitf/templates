from sqlmodel import Field, Column, SQLModel

class Model(SQLModel, table=True):
    pass
