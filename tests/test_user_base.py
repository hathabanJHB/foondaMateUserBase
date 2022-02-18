import unittest
import user_base


class MyTestCase(unittest.TestCase):
    def test_getHttpData_correct(self):
       def test_getHttpData_correct(self):
        expected = str({
           "01-01-2022":300,
           "02-01-2022":500,
           "03-01-2022":700,
           "04-01-2022":1300,
           "05-01-2022":2000,
           "06-01-2022":3000,
           "15-01-2022":90000
           })
        results = user_base.getHttpData('http://127.0.0.1:5000/test')
        self.assertEqual(expected, results)


    def test_getHttpData_incorrect_url(self):
        url = 'http://127.0.8659580.1:5000/test'
        expected = f"""Error: Unable to get userbase. try the following:
            - check your internet connection
            - check if \"{url}\" is correct
            - retry
                    """
        results = user_base.getHttpData(url)
        self.assertEqual(expected, results)
    

    def test_dateFilter_correct(self):
        dates = ['10-2-2022', '1-3-2022', '5-3-2022', '5-4-2022', '6-4-2022', '7-4-2022', '6-5-2022']
        start_date = '1-3-2022'
        end_date = '6-4-2022'

        expected = ['1-3-2022', '5-3-2022', '5-4-2022', '6-4-2022']
        result = user_base.dateFilter(dates, start_date, end_date)
        self.assertEqual(expected, result)


    #test with invalid start date and wrong end date 
    def test_dateFilter_invalid(self):
        dates = ['10-2-2022', '1-3-2022', '5-3-2022', '5-4-2022', '6-4-2022', '7-4-2022', '6-5-2022']
        start_date = '1-3-2025'
        end_date = '6-4-2025'

        expected = []
        result = user_base.dateFilter(dates, start_date, end_date)
        self.assertEqual(expected, result)