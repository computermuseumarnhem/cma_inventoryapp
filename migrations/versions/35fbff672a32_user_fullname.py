"""user fullname

Revision ID: 35fbff672a32
Revises: d3e24dd9b0c5
Create Date: 2021-03-28 01:02:11.342047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35fbff672a32'
down_revision = 'd3e24dd9b0c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('fullname', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'fullname')
    # ### end Alembic commands ###
