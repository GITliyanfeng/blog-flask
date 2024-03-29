"""'add_archive'

Revision ID: 5ca8ead6a275
Revises: 63b8ef44994b
Create Date: 2019-01-03 00:01:23.272184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ca8ead6a275'
down_revision = '63b8ef44994b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('archives',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_archives_name'), 'archives', ['name'], unique=False)
    op.add_column('posts', sa.Column('arc_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'archives', ['arc_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'arc_id')
    op.drop_index(op.f('ix_archives_name'), table_name='archives')
    op.drop_table('archives')
    # ### end Alembic commands ###
