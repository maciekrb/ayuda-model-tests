from datetime import datetime, timezone
import unittest

from ayuda.model import AyudaPlay


class TestAyudaModel(unittest.TestCase):
    def test_play_to_end_and_zero_design_duration_greater_than_zero(self):
        """ PlayToEnd True and DesignDuration > 0, use DesignDuration"""
        adPlay = AyudaPlay(
            **{
                "DigitalFaceCode": "FFM-Newslink-Flinders-St-S2",
                "SiteCode": "FFM-Newslink-Flinders-St",
                "MediaFileName": "3d2452e2-371e-4bf6-bf12-02c9cb235e31",
                "AdvertiserName": "Fairfax Media",
                "AdvertiserCode": "Fairfax Media ad",
                "SpotLength": 15,
                "PlayToEnd": True,
                "DesignDuration": 10,
                "EndTime": datetime(
                    year=2019,
                    month=4,
                    day=5,
                    hour=5,
                    minute=31,
                    second=44,
                    tzinfo=timezone.utc,
                ),
            }
        )

        self.assertEqual(10, adPlay._duration())
        self.assertEqual(
            datetime(2019, 4, 5, 5, 31, 34, tzinfo=timezone.utc), adPlay._start_time()
        )

    def test_play_to_end_and_zero_design_duration_greater_than_zero(self):
        """ PlayToEnd True and DesignDuration == 0, use SpotLength """
        adPlay = AyudaPlay(
            **{
                "DigitalFaceCode": "FFM-Newslink-Flinders-St-S2",
                "SiteCode": "FFM-Newslink-Flinders-St",
                "MediaFileName": "3d2452e2-371e-4bf6-bf12-02c9cb235e31",
                "AdvertiserName": "Fairfax Media",
                "AdvertiserCode": "Fairfax Media ad",
                "SpotLength": 15,
                "PlayToEnd": True,
                "DesignDuration": 0,
                "EndTime": datetime(
                    year=2019,
                    month=4,
                    day=5,
                    hour=5,
                    minute=31,
                    second=44,
                    tzinfo=timezone.utc,
                ),
            }
        )

        self.assertEqual(15, adPlay._duration())
        self.assertEqual(
            datetime(2019, 4, 5, 5, 31, 29, tzinfo=timezone.utc), adPlay._start_time()
        )

    def test_no_play_to_end_and_zero_design_duration(self):
        """ Play to End False and design Duration == 0, use SpotLength """
        adPlay = AyudaPlay(
            **{
                "DigitalFaceCode": "FFM-Newslink-Flinders-St-S2",
                "SiteCode": "FFM-Newslink-Flinders-St",
                "MediaFileName": "3d2452e2-371e-4bf6-bf12-02c9cb235e31",
                "AdvertiserName": "Fairfax Media",
                "AdvertiserCode": "Fairfax Media ad",
                "SpotLength": 15,
                "PlayToEnd": False,
                "DesignDuration": 0,
                "EndTime": datetime(
                    year=2019,
                    month=4,
                    day=5,
                    hour=5,
                    minute=31,
                    second=44,
                    tzinfo=timezone.utc,
                ),
            }
        )

        self.assertEqual(15, adPlay._duration())
        self.assertEqual(
            datetime(2019, 4, 5, 5, 31, 29, tzinfo=timezone.utc), adPlay._start_time()
        )

    def test_no_play_to_end_and_design_duration_lower_than_spot_length(self):
        """ Play to End False and design Duration lower than SpotLength,
        use DesignDuration """

        adPlay = AyudaPlay(
            **{
                "DigitalFaceCode": "FFM-Newslink-Flinders-St-S2",
                "SiteCode": "FFM-Newslink-Flinders-St",
                "MediaFileName": "3d2452e2-371e-4bf6-bf12-02c9cb235e31",
                "AdvertiserName": "Fairfax Media",
                "AdvertiserCode": "Fairfax Media ad",
                "SpotLength": 15,
                "PlayToEnd": False,
                "DesignDuration": 10,
                "EndTime": datetime(
                    year=2019,
                    month=4,
                    day=5,
                    hour=5,
                    minute=31,
                    second=44,
                    tzinfo=timezone.utc,
                ),
            }
        )

        self.assertEqual(10, adPlay._duration())
        self.assertEqual(
            datetime(2019, 4, 5, 5, 31, 34, tzinfo=timezone.utc), adPlay._start_time()
        )

    def test_no_play_to_end_and_design_duration_equal_to_spot_length(self):
        """ Edge case defaulting to SpotLength """

        adPlay = AyudaPlay(
            **{
                "DigitalFaceCode": "FFM-Newslink-Flinders-St-S2",
                "SiteCode": "FFM-Newslink-Flinders-St",
                "MediaFileName": "3d2452e2-371e-4bf6-bf12-02c9cb235e31",
                "AdvertiserName": "Fairfax Media",
                "AdvertiserCode": "Fairfax Media ad",
                "SpotLength": 15,
                "PlayToEnd": False,
                "DesignDuration": 15,
                "EndTime": datetime(
                    year=2019,
                    month=4,
                    day=5,
                    hour=5,
                    minute=31,
                    second=44,
                    tzinfo=timezone.utc,
                ),
            }
        )

        self.assertEqual(15, adPlay._duration())
        self.assertEqual(
            datetime(2019, 4, 5, 5, 31, 29, tzinfo=timezone.utc), adPlay._start_time()
        )

    def test_no_play_to_end_and_design_duration_greater_than_spot_length(self):
        """ Edge case defaulting to SpotLength """

        adPlay = AyudaPlay(
            **{
                "DigitalFaceCode": "FFM-Newslink-Flinders-St-S2",
                "SiteCode": "FFM-Newslink-Flinders-St",
                "MediaFileName": "3d2452e2-371e-4bf6-bf12-02c9cb235e31",
                "AdvertiserName": "Fairfax Media",
                "AdvertiserCode": "Fairfax Media ad",
                "SpotLength": 15,
                "PlayToEnd": False,
                "DesignDuration": 20,
                "EndTime": datetime(
                    year=2019,
                    month=4,
                    day=5,
                    hour=5,
                    minute=31,
                    second=44,
                    tzinfo=timezone.utc,
                ),
            }
        )

        self.assertEqual(15, adPlay._duration())
        self.assertEqual(
            datetime(2019, 4, 5, 5, 31, 29, tzinfo=timezone.utc), adPlay._start_time()
        )
