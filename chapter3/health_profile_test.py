import unittest

from . import health_profile


class HealthProfileTest(unittest.TestCase):
    def test_that_class_can_be_created(self):
        clinic = health_profile.Hospital('Maryland')
        self.assertIsNotNone(clinic)
        self.assertIsInstance(clinic, health_profile.Hospital)

    def class_can_check_for_patient_record(self):
        clinic = health_profile.Hospital('Maryland')
        clinic.get_patient_record()


if __name__ == '__main__':
    unittest.main()
