"""empty message

Revision ID: fc9310c14041
Revises: 54892bfc5a38
Create Date: 2020-11-14 20:21:34.853700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc9310c14041'
down_revision = '54892bfc5a38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tarefa', sa.Column('projeto_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tarefa', 'projeto', ['projeto_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tarefa', type_='foreignkey')
    op.drop_column('tarefa', 'projeto_id')
    # ### end Alembic commands ###
