from sqlmodel import SQLModel


class Model(SQLModel, table=True):
    pass
