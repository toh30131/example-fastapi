"""add last few columns to posts table

Revision ID: b36a02e32ec3
Revises: 806b02ad1000
Create Date: 2023-06-21 22:16:55.465192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b36a02e32ec3'
down_revision = '806b02ad1000'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post', sa.Column('published', sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column('post', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('post','published')
    op.drop_column('post', 'created_at')
    pass
