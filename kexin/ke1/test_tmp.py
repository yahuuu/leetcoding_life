# a = [1, 2, 3, 4, 5, 6]
# ls = filter(lambda x:3<=x<=5, a)
# print(list(ls))


class AException(Exception):
    def __str__(self):
        return "catch A"
class BException(AException):
    def __str__(self):
        return "catch B"

try:
    try:
        raise AException()
    except BException:
        raise
except Exception as exc:
    print(str(exc))

