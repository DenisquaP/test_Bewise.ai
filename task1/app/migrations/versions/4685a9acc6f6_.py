"""empty message

Revision ID: 4685a9acc6f6
Revises: 
Create Date: 2023-05-22 21:03:46.436230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4685a9acc6f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.Column('created at', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('question_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    # ### end Alembic commands ###
