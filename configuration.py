# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Configuration']


class Configuration:
    __metaclass__ = PoolMeta
    __name__ = 'work.configuration'
    work_sequence = fields.Property(fields.Many2One('ir.sequence',
            'Work Sequence', domain=[
                ('code', '=', 'project.work'),
                ]))
