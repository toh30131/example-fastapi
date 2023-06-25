"""create post table

Revision ID: e9f97382c136
Revises: 
Create Date: 2023-06-19 21:34:48.377508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9f97382c136'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('post',sa.Column("id", sa.Integer(), nullable=False, primary_key=True)
                    , sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('post')
    pass
