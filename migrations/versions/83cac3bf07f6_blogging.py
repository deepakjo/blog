"""blogging

Revision ID: 83cac3bf07f6
Revises: 9f74adbbbb94
Create Date: 2019-11-15 06:52:08.134055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83cac3bf07f6'
down_revision = '9f74adbbbb94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('is_blog', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('tags', sa.String(length=32), nullable=True))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), nullable=True))

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('tags')
        batch_op.drop_column('is_blog')
        batch_op.drop_column('description')

    # ### end Alembic commands ###
