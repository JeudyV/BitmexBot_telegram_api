"""empty message

Revision ID: 89681dd78d15
Revises: 
Create Date: 2020-01-28 07:20:49.673965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89681dd78d15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('userID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('apikey', sa.String(length=50), nullable=False),
    sa.Column('apisecret', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('userID')
    )
    op.create_table('lists_',
    sa.Column('idlist', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('name_list', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['users.userID'], ),
    sa.PrimaryKeyConstraint('idlist')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lists_')
    op.drop_table('users')
    # ### end Alembic commands ###
