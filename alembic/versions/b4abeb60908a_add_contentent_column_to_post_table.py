"""add contentent column to post table

Revision ID: b4abeb60908a
Revises: e9f97382c136
Create Date: 2023-06-19 22:42:25.573434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4abeb60908a'
down_revision = 'e9f97382c136'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("post", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("post", "content")
    pass
