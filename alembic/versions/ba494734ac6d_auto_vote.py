"""auto-vote

Revision ID: ba494734ac6d
Revises: 14aeaf9a446f
Create Date: 2024-12-27 21:07:10.936918

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba494734ac6d'
down_revision: Union[str, None] = '14aeaf9a446f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.alter_column('posts', 'content',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('posts', 'published',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=False)
    op.drop_constraint('post_users_fk', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['owner_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('post_users_fk', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.alter_column('posts', 'published',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('posts', 'content',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
    op.drop_table('votes')
    # ### end Alembic commands ###
