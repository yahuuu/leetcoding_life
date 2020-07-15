# -*- coding:utf-8 -*-
# Created data:

"""
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1;




# limit n子句表示查询结果返回前n条数据
#
# offset n表示跳过x条语句
#
# limit y offset x 分句表示查询结果跳过 x 条数据，读取前 y 条数据
#
# 作者：houzidata
# 链接：https://leetcode-cn.com/problems/second-highest-salary/solution/tu-jie-sqlmian-shi-ti-ru-he-cha-zhao-di-ngao-de-sh/
"""
