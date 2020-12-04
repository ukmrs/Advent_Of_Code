from functools import partial
import re


def validate_least_most(at_least, at_most, byr) -> bool:
    try:
        return at_least <= int(byr) <= at_most
    except TypeError:
        return False


vbyr = partial(validate_least_most, 1920, 2002)
viyr = partial(validate_least_most, 2010, 2020)
veyr = partial(validate_least_most, 2020, 2030)

# -----------------------------------------------------------
_hgtex = re.compile(r"(\d+)(cm|in)")
_hclex = re.compile(r"^#[a-f0-9]{6}$")
_pidex = re.compile(r"^\d{9}$")
_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
# -----------------------------------------------------------


def vhgt(hgt):
    try:
        height, unit = _hgtex.match(hgt).groups()
    except AttributeError:
        return False

    if unit == "cm":
        return validate_least_most(150, 193, height)
    return validate_least_most(59, 76, height)


def vhcl(hcl):
    return bool(_hclex.match(hcl))


def vpid(pid):
    return bool(_pidex.match(pid))


def vecl(ecl):
    return ecl in _eye_colors


airport_scanner = {
    "byr": vbyr,
    "iyr": viyr,
    "hcl": vhcl,
    "eyr": veyr,
    "hgt": vhgt,
    "ecl": vecl,
    "pid": vpid,
    "cid": lambda _: True
}


def test():
    assert _pidex.match("000000999")
    assert not _pidex.match("0000009991")
    assert not _pidex.match("00000999")


if __name__ == "__main__":
    vhgt("120m")
    test()
