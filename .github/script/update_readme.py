import requests

# 사용자 이름 설정
username = "hojoonSong"

# GitHub API로부터 저장소 목록을 가져옵니다.
response = requests.get(f"https://api.github.com/users/{username}/repos")
repos = response.json()

# 언어 데이터를 저장할 딕셔너리
languages = {}

# 각 저장소에 대해 반복
for repo in repos:
    # 저장소 이름
    repo_name = repo['name']
    # 저장소의 언어 데이터를 가져옵니다.
    response = requests.get(f"https://api.github.com/repos/{username}/{repo_name}/languages")
    repo_languages = response.json()
    # 언어 데이터를 누적합니다.
    for language, lines in repo_languages.items():
        if language in languages:
            languages[language] += lines
        else:
            languages[language] = lines

# 언어 데이터 출력
print(languages)

# README.md 파일 생성 또는 업데이트
with open('README.md', 'w') as f:
    f.write("# 포트폴리오\n")
    f.write("## 사용한 언어들\n")
    for language, lines in sorted(languages.items(), key=lambda x: x[1], reverse=True):
        f.write(f"- {language}: {lines} lines\n")

# 이 스크립트는 로컬에서 실행되며, 생성된 README.md 파일을 GitHub에 push해야 합니다.
