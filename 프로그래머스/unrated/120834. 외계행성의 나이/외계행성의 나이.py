alpa_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def solution(age):
    age_split = list(map(int, str(age)))
    if age == 1000:
        return "baaa"
    elif 99 < int(age):
        return alpa_list[age_split[0]] + alpa_list[age_split[1]] + alpa_list[age_split[2]]
    elif 10 < int(age):
        return alpa_list[age_split[0]] + alpa_list[age_split[1]]
    else:
        return alpa_list[age_split[0]]