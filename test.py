from unittest import mock, TestCase, main

from app import GhanianName


class NameTestCase(TestCase):

    def test_weekday_name(self):
        app = GhanianName()
        app.gender = 'm'
        app.dob = '14/11/1972'
        self.assertEqual(app.get_weekday_name(), 'Tuesday')
    
    def test_dob_weekday_name(self):
        app=GhanianName()
        app.gender ='m'
        app.dob = '13/06/1998'
        self.assertEqual(app.get_ghanaian_name(),'Kwame')

if __name__ == '__main__':
    main()
