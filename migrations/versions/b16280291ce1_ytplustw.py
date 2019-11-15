"""ytPlustw

Revision ID: b16280291ce1
Revises: 16ea76e0bdd0
Create Date: 2017-11-04 02:59:45.148225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b16280291ce1'
down_revision = '16ea76e0bdd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('twTag', sa.String(length=32), nullable=True))
    op.add_column('posts', sa.Column('ytVideoId', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'ytVideoId')
    op.drop_column('posts', 'twTag')
    # ### end Alembic commands ###
