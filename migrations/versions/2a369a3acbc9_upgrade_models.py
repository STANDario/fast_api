"""Upgrade models

Revision ID: 2a369a3acbc9
Revises: df630fbfd488
Create Date: 2023-12-12 18:31:21.036032

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '2a369a3acbc9'
down_revision: Union[str, None] = 'df630fbfd488'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'birthday',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'birthday',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    # ### end Alembic commands ###
