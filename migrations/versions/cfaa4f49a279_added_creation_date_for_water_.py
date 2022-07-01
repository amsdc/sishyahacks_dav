"""Added creation date for water conservation

Revision ID: cfaa4f49a279
Revises: 0c66627502a5
Create Date: 2022-05-26 19:42:38.437794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfaa4f49a279'
down_revision = '0c66627502a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('water_conservation', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_water_conservation_created_on'), 'water_conservation', ['created_on'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_water_conservation_created_on'), table_name='water_conservation')
    op.drop_column('water_conservation', 'created_on')
    # ### end Alembic commands ###