"""'edit_post_model_add_desc'

Revision ID: 63b8ef44994b
Revises: e18f070061fb
Create Date: 2019-01-02 13:48:56.422342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63b8ef44994b'
down_revision = 'e18f070061fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('desc', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'desc')
    # ### end Alembic commands ###
