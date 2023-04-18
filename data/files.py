import datetime
import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Files(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'file'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    owner = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    type_f = sqlalchemy.Column(sqlalchemy.String, default='PDF')
    url_address = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False)
    user = orm.relationship('User')

    def __repr__(self):
        return f'<Job> {self.job}'
