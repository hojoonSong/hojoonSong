import requests
import urllib.parse

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

# 전체 코드 라인 수를 계산합니다.
total_lines = sum(languages.values())

# README.md 파일 생성 또는 업데이트
with open('README.md', 'w', encoding='utf-8') as f:
    f.write("# 포트폴리오\n\n")
    f.write("## 📚 기술 스택\n\n")
    
    # 각 언어에 대한 badge와 함께 사용량 정보를 작성합니다.
    for language, lines in sorted(languages.items(), key=lambda x: x[1], reverse=True):
        percentage = (lines / total_lines) * 100
        encoded_language = urllib.parse.quote(language)
        badge_url = f"https://img.shields.io/badge/{encoded_language}-{lines} lines ({percentage:.2f}%%)-informational?style=for-the-badge&logo={encoded_language.lower()}&logoColor=white"
        f.write(f"![{language} Badge]({badge_url})\n")

    f.write("\n\n## 언어 사용량\n\n")
    f.write("언어 | 코드 라인 수 | 퍼센테이지\n")
    f.write("--- | --- | ---\n")
    for language, lines in sorted(languages.items(), key=lambda x: x[1], reverse=True):
        percentage = (lines / total_lines) * 100
        f.write(f"{language} | {lines} | {percentage:.2f}%\n")

# 이 스크립트는 로컬에서 실행되며, 생성된 README.md 파일을 GitHub에 push해야 합니다.
