import re

# def count_general_patterns(text):
#     # 패턴1: b, 동일한 문자열, b, 동일한 문자열, b
#     # 패턴2: b, 임의의 문자열, b, 동일한 문자열, b
#     pattern1 = r'b(.*?)b\1b'
#     pattern2 = r'b(.+?)b(.+?)b'
#     # 모든 매칭된 패턴을 찾아서 두 개의 리스트로 저장
#     matches1 = re.findall(pattern1, text)
#     print(matches1)
#     matches2 = re.findall(pattern2, text)
#     print(matches2)
#     # 두 리스트의 합집합 개수를 반환 (중복을 허용하지 않음)
#     unique_matches = set(matches1 + matches2)
#     return len(unique_matches)

def count_length_matched_patterns(text):
    # 패턴: b, 정확히 두 개의 임의의 문자, b, 정확히 두 개의 임의의 문자, b
    # pattern = r'b(...)b(...)b'
    matches_count = 0
    for i in range(0, 4):
        pattern = r'b({})b({})b'.format('.' * i, '.' * i)
        matches = re.findall(pattern, text)
        print(matches)
        matches_count += len(matches)
    return matches_count

# 문자열을 정의합니다.
# text = "aaabbbcbbaaa"     # 2
# text = "aaabbbccbaaa"     # 1
# text = "aaabbbbcabaa"       # 2
text = "aaabbbbbaaab"

# 함수를 호출하여 결과를 출력합니다.
occurrences = count_length_matched_patterns(text)
print(f"'bbb' 패턴이 출현한 횟수: {occurrences}")
