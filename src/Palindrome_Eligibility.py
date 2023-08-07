# "dj{qsqs(sqs)[qq{wdwdw}]sqsq}" --- Valid
# "sa{sq{q[qjgsq(s)s]s}" --- Invalid
# "{sqs[sq)sqs]sqs}" --- Invalid
# "{jgj[jhj(jgjg)kh)]}" --- Invalid


# abacedbce == > abcedecba
# xxxxzzy == > xxzyzxx
# abab == > abba
# aaa == > aaa
# baa == > aba
# gg == > gg


def is_palindrome_eligible_string(sample_string):
    count_dict = {}
    count = 0
    for item in sample_string:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    for key in count_dict:
        if count_dict[key] % 2 != 0:
            count = count + 1
        if count > 1:
            print("Not Eligible")
            break
        else:
            print("Eligible")


is_palindrome_eligible_string('papo')
