from datetime import datetime
import sqlalchemy as sa
import sqlalchemy.orm as so
from board.extensions import db


class Post(db.Model):
    __tablename__ = 'post'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    created: so.Mapped[sa.DateTime] = so.mapped_column(sa.DateTime, 
            default=datetime.utcnow, nullable=False)
    author: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)
    message: so.Mapped[str] = so.mapped_column(sa.String, nullable=False)

    def __repr__(self):
            return f"<Post(author='{self.author}', message='{self.message}')>"