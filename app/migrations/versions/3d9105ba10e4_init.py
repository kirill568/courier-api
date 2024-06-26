"""init

Revision ID: 3d9105ba10e4
Revises: 
Create Date: 2024-05-23 15:06:52.790854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d9105ba10e4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courier',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_courier_id'), 'courier', ['id'], unique=False)
    op.create_table('district',
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_district_id'), 'district', ['id'], unique=False)
    op.create_table('district_courier',
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('courier_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['courier_id'], ['courier.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['district_id'], ['district.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_district_courier_id'), 'district_courier', ['id'], unique=False)
    op.create_table('order',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('courier_id', sa.Integer(), nullable=True),
    sa.Column('district_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('finish_date', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['courier_id'], ['courier.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['district_id'], ['district.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_finish_date'), 'order', ['finish_date'], unique=False)
    op.create_index(op.f('ix_order_id'), 'order', ['id'], unique=False)
    op.create_index(op.f('ix_order_start_date'), 'order', ['start_date'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_order_start_date'), table_name='order')
    op.drop_index(op.f('ix_order_id'), table_name='order')
    op.drop_index(op.f('ix_order_finish_date'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_district_courier_id'), table_name='district_courier')
    op.drop_table('district_courier')
    op.drop_index(op.f('ix_district_id'), table_name='district')
    op.drop_table('district')
    op.drop_index(op.f('ix_courier_id'), table_name='courier')
    op.drop_table('courier')
    # ### end Alembic commands ###
