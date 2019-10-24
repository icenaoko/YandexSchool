from bank import creditCalculator
import unittest as ut

class CreditCalculatorTests(ut.TestCase):
    # конкретный тест
    def test_wrong_age_data_type(self):
        self.assertEqual(creditCalculator('N/A', 'F', 'employee', 2, -1, 1, 5, 'mortgage'), 'Data validation fails')

    def test_wrong_sex_data_type(self):
        self.assertEqual(creditCalculator(18, 'N/A', 'employee', 2, -1, 1, 5, 'mortgage'), 'Data validation fails')

    def test_correct_passive_income_source(self):
        self.assertEqual(creditCalculator(18, 'F', 'passive', 2, 2, 1, 5, 'mortgage'), list(['Approved', 0.2775]))

    def test_correct_employee_income_source(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 1, 5, 'mortgage'), list(['Approved', 0.2925]))

    def test_correct_self_employed_income_source(self):
        self.assertEqual(creditCalculator(18, 'F', 'self-employed', 3, 2, 10, 20, 'mortgage'), list(['Approved', 1.15]))

    def test_wrong_income_source(self):
        self.assertEqual(creditCalculator(18, 'F', 'N/A', 2, -1, 1, 5, 'mortgage'), 'Data validation fails')

    def test_wrong_income(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 0, -1, 1, 5, 'mortgage'), 'Data validation fails')

    def test_wrong_credit_rating_under_lower_bound(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -3, 1, 5, 'mortgage'), 'Data validation fails')

    def test_correct_zero_credit_rating(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, 0, 1, 5, 'mortgage'), list(['Approved', 0.2775]))

    def test_correct_one_credit_rating(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, 1, 1, 5, 'mortgage'), list(['Approved', 0.275]))

    def test_correct_two_credit_rating(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, 2, 5, 10, 'mortgage'), list(['Approved', 0.8151]))

    def test_wrong_credit_rating_above_apper_bound(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, 3, 1, 5, 'mortgage'), 'Data validation fails')

    def test_wrong_credit_rating(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, 'N/A', 1, 5, 'mortgage'), 'Data validation fails')

    def test_wrong_requested_sum_under_lower_bound(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 0.01, 5, 'mortgage'), 'Data validation fails')

    def test_wrong_requested_sum_above_apper_bound(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 11, 5, 'mortgage'), 'Data validation fails')

    def test_wrong_requested_sum(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 'N/A', 5, 'mortgage'), 'Data validation fails')

    def test_wrong_duration_under_lower_bound(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 1, 0.1, 'mortgage'), 'Data validation fails')

    def test_wrong_duration(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 1, 'N/A', 'mortgage'), 'Data validation fails')

    def test_correct_business_purpose(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 1, 5, 'business'), list(['Approved', 0.3075]))

    def test_correct_car_purpose(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 1, 5, 'car'), list(['Approved', 0.3125]))

    def test_correct_consumer_purpose(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 1, 5, 'consumer'), list(['Approved', 0.3275]))

    def test_wrong_purpose(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 1, 5, 'N/A'), 'Data validation fails')

    def test_wrong_pension_age_female(self):
        self.assertEqual(creditCalculator(56, 'F', 'employee', 2, -1, 1, 5, 'mortgage'), 'Credit application denied')

    def test_wrong_pension_male(self):
        self.assertEqual(creditCalculator(61, 'F', 'employee', 2, -1, 1, 5, 'mortgage'), 'Credit application denied')

    def test_wrong_age_underage(self):
        self.assertEqual(creditCalculator(15, 'F', 'employee', 2, -1, 1, 5, 'mortgage'), 'Credit application denied')

    def test_wrong_requested_sum_more_than_third_of_income(self):
       self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 3, 3, 'mortgage'), 'Credit application denied')

    def test_wrong_low_credit_rating(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -2, 1, 5, 'mortgage'), 'Credit application denied')

    def test_wrong_income_source_unemployed(self):
        self.assertEqual(creditCalculator(18, 'F', 'unemployed', 2, -1, 1, 5, 'mortgage'), 'Credit application denied')

    def test_wrong_yearly_payment_mora_than_half_of_income(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 1, 0, 3, 9, 'mortgage'), 'Credit application denied')

    def test_wrong_requested_sum_more_than_allowed_passive_income_source(self):
        self.assertEqual(creditCalculator(18, 'F', 'passive', 2, 2, 2, 5, 'mortgage'), 'Credit application denied')

    def test_wrong_requested_sum_more_than_allowed_employee_income_source(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, 2, 5.1, 10, 'mortgage'), 'Credit application denied')

    def test_wrong_requested_sum_more_than_allowed_minus_one_credit_rating(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, -1, 1.1, 5, 'mortgage'), 'Credit application denied')

    def test_wrong_requested_sum_more_than_allowed_zero_creadit_rating(self):
        self.assertEqual(creditCalculator(18, 'F', 'employee', 2, 0, 5.2, 5, 'mortgage'), 'Credit application denied')

# запускалка тестов, будет ранить все тесты внутри классов унаследованных от ut.TestCase
# запускаем так: python3 test.py
if __name__ == "__main__":
    ut.main()
