"""add content column to posts table

Revision ID: 3981f339e202
Revises: f521067ef2e3
Create Date: 2023-09-01 19:12:11.914928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3981f339e202'
down_revision: Union[str, None] = 'f521067ef2e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("content", sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_column("posts", "content")
