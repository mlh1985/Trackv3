"""Add race_id to Car model

Revision ID: 5b1f4c72ce75
Revises: <previous_revision_id>
Create Date: 2024-06-20 08:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b1f4c72ce75'
down_revision = '<previous_revision_id>'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.add_column(sa.Column('race_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_car_race', 'race', ['race_id'], ['id'])


def downgrade():
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.drop_constraint('fk_car_race', type_='foreignkey')
        batch_op.drop_column('race_id')
