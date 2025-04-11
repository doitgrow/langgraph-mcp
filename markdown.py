import json
import os
import sys

def json_to_markdown(json_file):
    # JSON 파일 읽기 (UTF-8 인코딩)
    with open(json_file, 'r', encoding='utf-8') as file:
        news_list = json.load(file)
    
    # Markdown 형식의 게시글 생성
    markdown_output = "# 오늘의 주요 뉴스\n\n"
    for idx, article in enumerate(news_list, start=1):
        markdown_output += f"### {idx}. {article['title']}\n"
        markdown_output += f"URL: {article['url']}\n"
        markdown_output += f"요약: {article['summary']}\n\n"
    
    # 입력 JSON 파일명에서 확장자를 제거하고 .md 확장자로 변경
    base_name = os.path.splitext(json_file)[0]
    md_file = f"{base_name}.md"
    
    # Markdown 파일로 저장
    with open(md_file, 'w', encoding='utf-8') as file:
        file.write(markdown_output)
    
    print(f"Markdown 파일 '{md_file}' 저장 완료!")

if __name__ == '__main__':
    # 커맨드라인 인자로 json 파일명을 받음
    
    input_json = "news_summary.json"
    json_to_markdown(input_json)
