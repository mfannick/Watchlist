"""Initial Migration

Revision ID: 359fd1647978
Revises: c8d8fd4d6cea
Create Date: 2019-09-19 15:34:24.088585

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '359fd1647978'
down_revision = 'c8d8fd4d6cea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('movie_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('image_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('movie_review', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='reviews_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    )
    # ### end Alembic commands ###
