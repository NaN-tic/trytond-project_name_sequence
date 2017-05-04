# This file is part project_name_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.tests.test_tryton import suite as test_suite
from trytond.pool import Pool
from trytond.modules.company.tests import create_company, set_company


class ProjectNameSequenceTestCase(ModuleTestCase):
    'Test Project Name Sequence module'
    module = 'project_name_sequence'

    @with_transaction()
    def test_project_name_sequence(self):
        "Test Project Name Sequence"
        pool = Pool()
        ProjectWork = pool.get('project.work')

        company = create_company()
        with set_company(company):
            p_work, = ProjectWork.create([{
                        'company': company.id,
                        }])
            self.assertEqual(p_work.name, '1')
            p_work2, = ProjectWork.copy([p_work])
            self.assertEqual(p_work2.name, '2')

def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            ProjectNameSequenceTestCase))
    return suite
