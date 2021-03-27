class Solution:
    def __init__(self):
        self.info_dict = {}

    def get_active_user_num(self, logs):
        self.log_2_dict(logs)
        month_num = str(self.count_month())
        day_num = self.count_day()
        print(month_num)
        print(day_num)
        return []

    def log_2_dict(self, logs):
        for ele in logs:
            daytime, usr_ip, web, flag = ele.strip().split("|")
            if not self.web_right(web):
                continue
            if not self.flag_success(flag):
                continue
            _, month, day = daytime.split("-")
            ip_string = self.usr_ip_rebuild(usr_ip)
            if self.info_dict.get(month, None) is None:
                self.info_dict[month] = {}
            if self.info_dict[month].get(day, None) is None:
                self.info_dict[month][day] = set()
            self.info_dict[month][day].add(ip_string)

    def usr_ip_rebuild(self, usr_ip):
        ls = usr_ip.split(".")
        ls_str_no_zero = [str(int(i)) for i in ls]
        return "".join(ls_str_no_zero)

    def flag_success(self, flag):
        if flag.strip() == "success":
            return True
        return False

    def web_right(self, web):
        if web == "/login.do":
            return True
        return False

    def count_month(self):
        return len(self.info_dict.keys())

    # { month : { day { ip1, ip2}}}
    def count_day(self):
        _res = [0]*12
        for month in self.info_dict.keys():
            _ip_num = 0
            for day in self.info_dict[month].keys():
                _ip_num += len(self.info_dict[month][day])
            _res[int(month)-1] = _ip_num
        return _res


if __name__ == "__main__":
    n = int(input().strip())
    logs = [input().strip() for _ in range(n)]
    function = Solution()
    results = function.get_active_user_num(logs)
    print(str.join(" ", map(str, results)))
