"""add foreign-key to posts table

Revision ID: 806b02ad1000
Revises: b899a544892a
Create Date: 2023-06-21 22:01:47.287202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '806b02ad1000'
down_revision = 'b899a544892a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('post',sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="post", referent_table="users",local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="post")
    op.drop_column('post','owner_id')
    pass
