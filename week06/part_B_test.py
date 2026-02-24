########################################################################
#                                       #                              #
# TESTING CODE FOR WEEK 06 ASSIGNMENT.  #  Testing code requires       #
# ADD THIS CODE AFTER YOUR WEEKO6 CODE. #  classes Concert and         #
# DO NOT MODIFY THE TESTING CODE.       #  Lecture to be present.      #
#                                       #                              #
########################################################################

import unittest  # Authorized import for unit testing
from time import time_ns  # Authorized import for timing
from __future__ import annotations  # Authorized import for type hints

from week06 import Performance, Concert, Lecture   # Authorized import for testing

import unittest


class TestConcert(unittest.TestCase):
    def test_concert_stores_additional_fields(self) -> None:
        c = Concert("Summer Blast", 120, 50.0, "The Meteors", "Rock", True)
        # "Protected" fields are still accessible in tests; this verifies
        # they were stored correctly.
        self.assertEqual("The Meteors", c._artist_name)
        self.assertEqual("Rock", c._genre)
        self.assertTrue(c._has_vip)

    def test_concert_revenue_no_audience_is_zero(self) -> None:
        c = Concert("Summer Blast", 120, 50.0, "The Meteors", "Rock", False)
        self.assertEqual(0.0, c.calculate_revenue())

    def test_concert_revenue_no_vip(self) -> None:
        c = Concert("Summer Blast", 120, 50.0, "The Meteors", "Rock", False)
        c.admit_audience(100)
        self.assertAlmostEqual(100 * 50.0, c.calculate_revenue(), places=7)

    def test_concert_revenue_with_vip_increases_40_percent(self) -> None:
        c = Concert("Summer Blast", 120, 50.0, "The Meteors", "Rock", True)
        c.admit_audience(100)
        # VIP increases ticket price by 40% -> multiplier 1.4
        self.assertAlmostEqual(100 * (50.0 * 1.4), c.calculate_revenue(), places=7)

    def test_concert_describe_mentions_artist_and_genre(self) -> None:
        c = Concert("Summer Blast", 120, 50.0, "The Meteors", "Rock", True)
        s = c.describe()
        self.assertIn("The Meteors", s)
        self.assertIn("Rock", s)

    def test_concert_str_uses_describe(self) -> None:
        c = Concert("Summer Blast", 120, 50.0, "The Meteors", "Rock", True)
        self.assertEqual(c.describe(), str(c))


class TestLecture(unittest.TestCase):
    def test_lecture_stores_additional_fields(self) -> None:
        """
        Spec requires:
          - speaker_name: str
          - is_university_event: bool

        If your Lecture currently uses a different field name (e.g.
        has_student_discount), these tests will (intentionally) fail until
        you align the implementation to the spec.
        """
        lec = Lecture("AI and Society", 90, 30.0, "Dr. Kwan", True)
        self.assertEqual("Dr. Kwan", lec._speaker_name)
        # Spec field name:
        self.assertTrue(lec.has_student_discount)

    def test_lecture_revenue_no_audience_is_zero(self) -> None:
        lec = Lecture("AI and Society", 90, 30.0, "Dr. Kwan", True)
        self.assertEqual(0.0, lec.calculate_revenue())

    def test_lecture_revenue_university_event_discount_50_percent(self) -> None:
        """
        Spec:
          If it’s a university event -> tickets discounted 50%
          revenue = audience_count * (base_ticket_price * 0.5)
        """
        lec = Lecture("AI and Society", 90, 30.0, "Dr. Kwan", True)
        lec.admit_audience(100)
        self.assertAlmostEqual(100 * (30.0 * 0.5), lec.calculate_revenue(), places=7)

    def test_lecture_revenue_not_university_event_no_discount(self) -> None:
        lec = Lecture("AI and Society", 90, 30.0, "Dr. Kwan", False)
        lec.admit_audience(100)
        self.assertAlmostEqual(100 * 30.0, lec.calculate_revenue(), places=7)

    def test_lecture_describe_mentions_speaker(self) -> None:
        lec = Lecture("AI and Society", 90, 30.0, "Dr. Kwan", True)
        s = lec.describe()
        self.assertIn("Dr. Kwan", s)

    def test_lecture_str_uses_describe(self) -> None:
        lec = Lecture("AI and Society", 90, 30.0, "Dr. Kwan", True)
        self.assertEqual(lec.describe(), str(lec))


class TestPolymorphismList(unittest.TestCase):
    def test_total_revenue_across_mixed_performances(self) -> None:
        events: list[Performance] = [
            Concert("Summer Blast", 120, 50.0, "The Meteors", "Rock", True),
            Lecture("AI and Society", 90, 30.0, "Dr. Kwan", True),
        ]

        for e in events:
            e.admit_audience(100)

        total = 0.0
        for e in events:
            total += e.calculate_revenue()

        expected = (100 * (50.0 * 1.4)) + (100 * (30.0 * 0.5))
        self.assertAlmostEqual(expected, total, places=7)


################################################################################
# fmt: off
#
# If you test in a .PY file, uncomment TEST-LINE-1 and TEST-LINE-2 and
# comment out TEST-LINE-3 to run the tests.

# if __name__ == "__main__":              #   TEST-LINE-1
#    unittest.main()                     #   TEST-LINE-2

# If you test in a Jupyter notebook, comment out TEST-LINE-1 and TEST-LINE-2
# and uncomment TEST-LINE-3 to run the tests in the notebook.

# unittest.main(argv=[''], exit=False)    #   TEST-LINE-3

################################################################################
