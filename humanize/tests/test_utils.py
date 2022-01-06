import pytest
from humanize.utils import do_humanize, get_text_for_magnitude


class TestDoHumanize:
    def test_zero(self):
        assert do_humanize(0) == "zero"

    def test_values(self):
        assert (
            do_humanize(12345678)
            == "twelve million three hundred forty five thousand six hundred seventy eight"
        )
        assert do_humanize(12) == "twelve"
        assert do_humanize(6) == "six"
        assert do_humanize(317) == "three hundred seventeen"
        assert do_humanize(634) == "six hundred thirty four"
        assert do_humanize(10 ** 3) == "one thousand"
        assert do_humanize(2 * 10 ** 6) == "two million"
        assert do_humanize(3 * 10 ** 9) == "three billion"
        # sys.maxsize
        assert (
            do_humanize(9223372036854775807)
            == "nine quintillion two hundred twenty three quadrillion three hundred seventy two trillion thirty six billion eight hundred fifty four million seven hundred seventy five thousand eight hundred seven"
        )

    def test_negative(self):
        assert (
            do_humanize(-12345678)
            == "negative twelve million three hundred forty five thousand six hundred seventy eight"
        )


class TestGetTextForMagnitude:
    def test_values(self):
        assert get_text_for_magnitude(1) == "one"
        assert get_text_for_magnitude(15) == "fifteen"
        assert get_text_for_magnitude(405) == "four hundred five"
        assert get_text_for_magnitude(617) == "six hundred seventeen"

    def test_errors(self):
        with pytest.raises(ValueError):
            get_text_for_magnitude(0)

        with pytest.raises(ValueError):
            get_text_for_magnitude(-2)

        with pytest.raises(ValueError):
            get_text_for_magnitude(10 ** 3)
