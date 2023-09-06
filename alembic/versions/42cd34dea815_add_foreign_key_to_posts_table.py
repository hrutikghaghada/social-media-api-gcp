"""add foreign-key to posts table

Revision ID: 42cd34dea815
Revises: d695b0a62b2d
Create Date: 2023-09-01 19:31:06.508790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42cd34dea815'
down_revision: Union[str, None] = 'd695b0a62b2d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
