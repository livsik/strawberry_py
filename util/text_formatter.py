from xc_testcase import TestCase
from result_formatter import ResultFormatterBase
from meta_line import MetaLine

class TextResultFormatter(ResultFormatterBase):

  file_extension = "txt"

  def format_result(self, test_cases):
    lines = ["Testsuite:\n",
             "----------\n"]

    num_fail = 0
    num_pass = 0
    sum_duration = 0

    for tc in test_cases:
      duration = 0
      err_log = ""
      for ml in tc.output:
        if ml.prefix == "Duration":
          duration = float(ml.body)
        elif ml.prefix == "Fail" or ml.prefix == "Error":
          err_log += "%s: %s" % (ml.prefix, ml.body)

      lines += ["testcase: %s, result: %s, time: %s\n" % (tc.file_name, tc.result, duration)]
      if tc.result:
        num_pass += 1
      else:
        num_fail += 1
      sum_duration += duration

    lines += ["Summary: failed: %s, passed: %s, total: %s, time: %s" % (num_fail, num_pass, (num_fail + num_pass), sum_duration)]

    return lines
