"""empty message

Revision ID: 704794c0746c
Revises: 
Create Date: 2023-05-28 13:46:16.131761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '704794c0746c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('records',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('uuid', sa.String(), nullable=False),
    sa.Column('record', sa.LargeBinary(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    op.drop_table('users')
    # ### end Alembic commands ###
