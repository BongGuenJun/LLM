# 각종 서비스 모듈을 import해서 테스트
- .gitignore를 통해서 api_key가 저장된 .env파일을 숨김
## 1.GPT Test
- OpenAPI 를 통해 GPT에 질문을 보내고 답을 받아와 출력
- .env 파일에  api_key 코드 저장
- dotenv를 통해서 api_key 를 .env에서 가져옴
- response 를 통해서 질문을 보내고 답을 받아와 출력
## 2. Gradio
- Gradio1 : gradio를 통해 블록생산, 마크다운으로 문자 출력
- Gradio2 : 
