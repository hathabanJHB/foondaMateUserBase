import unittest
import user_base


class MyTestCase(unittest.TestCase):
    #@test dateFilter function
    def test_date_filter_correct(self):
        dates = ['10-2-2022', '1-3-2022', '5-3-2022', '5-4-2022', '6-4-2022', '7-4-2022', '6-5-2022']
        start_date = '1-3-2022'
        end_date = '6-4-2022'

        expected = ['1-3-2022', '5-3-2022', '5-4-2022', '6-4-2022']
        result = user_base.dateFilter(dates, start_date, end_date)
        self.assertEqual(expected, result)