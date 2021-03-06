"""empty message

Revision ID: 9485efb78f77
Revises: 
Create Date: 2021-07-06 22:11:31.818187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9485efb78f77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Personajes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('altura', sa.String(length=250), nullable=True),
    sa.Column('masa', sa.String(length=250), nullable=True),
    sa.Column('color_cabello', sa.String(length=250), nullable=True),
    sa.Column('color_piel', sa.String(length=250), nullable=True),
    sa.Column('color_ojos', sa.String(length=250), nullable=True),
    sa.Column('fecha_nacimiento', sa.String(length=250), nullable=True),
    sa.Column('genero', sa.String(length=250), nullable=True),
    sa.Column('creacion', sa.String(length=250), nullable=True),
    sa.Column('editado', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Planeta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('diametro', sa.String(length=250), nullable=True),
    sa.Column('periodo_rotacion', sa.String(length=250), nullable=True),
    sa.Column('periodo_orbital', sa.String(length=250), nullable=True),
    sa.Column('gravedad', sa.String(length=250), nullable=True),
    sa.Column('poblacion', sa.String(length=250), nullable=True),
    sa.Column('clima', sa.String(length=250), nullable=True),
    sa.Column('terreno', sa.String(length=250), nullable=True),
    sa.Column('superfice_acuatica', sa.String(length=250), nullable=True),
    sa.Column('creacion', sa.String(length=250), nullable=True),
    sa.Column('editado', sa.String(length=250), nullable=True),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planeta_id', sa.Integer(), nullable=True),
    sa.Column('personajes_id', sa.Integer(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['personajes_id'], ['Personajes.id'], ),
    sa.ForeignKeyConstraint(['planeta_id'], ['Planeta.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['Usuario.id'], ),
    sa.PrimaryKeyConstraint('id', 'usuario_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Favoritos')
    op.drop_table('Usuario')
    op.drop_table('Planeta')
    op.drop_table('Personajes')
    # ### end Alembic commands ###
