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
    f.write("## 🙋‍♂️ About Me\n\n")
    f.write("### 안녕하세요, 저는 **송호준**입니다.\n")
    f.write("_솔직한 마음을 표현하고, 다른 사람의 어려움을 이해하는 개발자입니다._\n")
    f.write("기술에 대한 깊은 이해와 함께 성장하고 싶은 동료들과 만나 성취를 즐기고 싶습니다.\n\n")

    f.write("### Hello, I am **Hojun Song**.\n")
    f.write("_A developer who values honesty and understands the challenges others face._\n")
    f.write("I look forward to growing alongside peers who share a deep understanding of technology and enjoying our achievements together.\n\n")

    f.write("### こんにちは、私は**ホジュンソン**です。\n")
    f.write("_正直な心を表現し、他人の困難を理解する開発者です。_\n")
    f.write("技術に対する深い理解を共有し、一緒に成長して成果を楽しみたいと考えています。\n\n")
    
    # 기술 스택 섹션 추가
    f.write("## 📚 Tech Stack\n\n")
    # 언어별 뱃지 생성
    for language, lines in sorted(languages.items(), key=lambda x: x[1], reverse=True):
        percentage = (lines / total_lines) * 100
        # URL 인코딩
        encoded_language = urllib.parse.quote(language)
        encoded_label = urllib.parse.quote(f"{language} - {lines} lines ({percentage:.2f}%)")
        badge_url = f"https://img.shields.io/badge/{encoded_label}-informational?style=flat&logo={encoded_language.lower()}"
        f.write(f"![{language} Badge]({badge_url})\n")
    
    # GitHub 통계 섹션 추가
    f.write("\n## 📈 GitHub Stats\n\n")
    f.write("![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=hojoonSong&show_icons=true&layout=compact&theme=radical)\n\n")
    f.write("![GitHub Stats](https://github-readme-stats.vercel.app/api?username=hojoonSong&show_icons=true&theme=radical)\n\n")
    
    # 블로그 및 소셜 미디어 링크 섹션 추가
    f.write("## 📝 Blog\n\n")
    f.write("[Visit my development blog](https://velog.io/@who_doctor)\n\n")
    
    f.write("## 🌐 Social\n\n")
    # 여기에 소셜 미디어 링크 추가
    # f.write("![Profile views](https://gpvc.arturio.dev/hojoonSong)\n")
    
    # 여기에 추가적인 소셜 뱃지를 추가할 수 있습니다.
