# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Work']


class Work:
    __metaclass__ = PoolMeta
    __name__ = 'project.work'

    @classmethod
    def __setup__(cls):
        super(Work, cls).__setup__()
        cls.name.required = False
        cls.name.readonly = True

    @classmethod
    def create(cls, vlist):
        pool = Pool()
        Sequence = pool.get('ir.sequence')
        Config = pool.get('work.configuration')

        vlist = [x.copy() for x in vlist]
        config = Config(1)
        for values in vlist:
            if not values.get('name') or (values.get('name') is None):
                values['name'] = Sequence.get_id(config.work_sequence)
        return super(Work, cls).create(vlist)

    @classmethod
    def copy(cls, works, default=None):
        if default is None:
            default = {}
        if 'name' not in default:
            default['name'] = None
        return super(Work, cls).copy(works, default)
