# 신고 결과 받기

# user 는 다른 user 를 신고
# user 가 한 user 를 여러번 신고할 수 있지만 1회로 처리
# 2번 이상 신고 당해야지만 정지

# 각 user 별로 신고하여 정지된 아이디 갯수 리턴

# id_list = ["muzi", "frodo", "apeach", "neo"]
# reports = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
id_list = ["con", "ryan"]
reports = ["ryan con", "ryan con", "ryan con", "ryan con"]

reported_count = {}
for id in id_list:
    reported_count[id] = 0

reported_info = {}
for report in reports:
    reporter = report.split(" ")[0]
    target = report.split(" ")[1]
    #
    add_target = False
    if reporter not in reported_info:
        reported_info[reporter] = set()
        add_target = True
    else:
        if not target in reported_info[reporter]:
            add_target = True
    #
    if add_target:
        reported_info[reporter].add(target)
        reported_count[target] += 1

answers = []
for id in id_list:
    mail_count = 0
    if id in reported_info:
        for target in reported_info[id]:
            if target in reported_count and reported_count[target] >= 2:
                mail_count += 1
    answers.append(mail_count)

print(reported_info)
print(reported_count)
print(answers)
