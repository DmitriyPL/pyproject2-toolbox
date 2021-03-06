"""empty message

Revision ID: 23595d2eeef4
Revises: 
Create Date: 2020-10-19 00:34:39.356672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23595d2eeef4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('days',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.String(), nullable=False),
    sa.Column('view', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.String(), nullable=False),
    sa.Column('view', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.String(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('about', sa.String(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=False),
    sa.Column('picture', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.String(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('days_relations',
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('day_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['day_id'], ['days.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], )
    )
    op.create_table('goals_relations',
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], )
    )
    op.create_table('times',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.Column('is_free', sa.Boolean(), nullable=False),
    sa.Column('day_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['day_id'], ['days.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('times')
    op.drop_table('goals_relations')
    op.drop_table('days_relations')
    op.drop_table('bookings')
    op.drop_table('teachers')
    op.drop_table('requests')
    op.drop_table('goals')
    op.drop_table('days')
    # ### end Alembic commands ###
