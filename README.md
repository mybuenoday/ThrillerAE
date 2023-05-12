# ThrillerAE
 구성원 - Bien(팀장), MJ, Elon<
 프로젝트 - openAI ChatBot을 이용하여 입력된 채용공고와 이력정보를 활용한 예상 면접 질문과 답변을 출력해주는 프로그램 제안
 
## 1. 개인 목표 및 역할
* mj - 웹개발 -> python코드로 작성한 함수를 html문서에서 구현, 
* Bien - 외부 api 연동
* Elon - 데이터 시각화

## 2. 팀명 Thriller Æ
* 스릴러와 같은 감동과 긴장감을 선사하는 프로젝트를 만드는 팀.
* Æ는 인공지능과 사랑을 상징하는 기호로, 라틴 문자 'ash’라고 읽습니다.

## 3. 아이디어 
* 채용 공고 링크/ 공고 내용 입력받기, 공고에 대한 면접 예상 질문 & 가능한 답변
- (Cancelled) LinkedIn 링크/이력 : social media access 불가.

<details> <summary>탈락된 아이디어</summary>
<p>
(1) 사주/mbti/ - 조건 넣고 gpt 답변 생성해 띄우기
- db 필요없음
- 입력받을 조건 지정
- ChatGPT에 조건, 어조 부여, 답변 생성

 (2) 효율적 일정관리 - 일정 매니저. 답변 내용 저장하여 외부 노트 연동 / 이메일 전송
- db 사용 또는 구글캘린더 등 연동
- ChatGPT에게 일정관리자 역할 부여. Scheduling Atuomation
- Reference: FlowSavvy
#### Reference 추천
- 조코딩, 장피엠, 챗지피터스, https://ktestone.com/kapable.github.io/labelSticker/
 </p>
 </details>
 
## 4. 계획<br>
(1) 아이디어 결정 - 5/4까지 (5/3은 reference 찾아보거나 상상 up)<br>
(2) 조건 창에 사용자 입력 받아 답변 생성 Python, ChatGPT api <br>
(3) html, js, css, python <br>
(4) 이미지 생성(MS Designer 등) 또는 첨부 / 디자인 요소 <br>

-------
## 5. Questions List
공고(Job Description)에 관한 것 + 본인에 대한 것

## 6. 개발 중 의문점
### Q. ChatGPT api가 공고 링크를 읽을 수 있는가?
- 링크드인 링크는 못 불러온다. (As an AI language model, I do not have the ability to access external websites or links. )
-> 공고글을 직접 복붙해와서 읽게 한다.
어라. 링크드인 공고 링크는 못 보는데, 회사 홈 공고 링크는 읽는다.

### Q. Linkedin 프로필 링크 읽어들일 수 있는가?
<details>
 <summary>* LinkedIn을 포함하여 소셜 미디어를 보안의 이유로 읽지 못하는 것 같다.</summary>
 <p>
As an AI language model, I cannot access LinkedIn profiles or any other social media platforms.
My programming is designed to ensure user privacy and data protection.

* Q: Can you read this: https://www.linkedin.com/jobs/view/3580115128 ?
- A: As an AI language model, I do not have the ability to access external websites or links.
However, based on the URL you provided, it appears to be a job listing on LinkedIn.
If you could provide me with more information about the job listing, I may be able to provide further assistance.

* Q: Can you read this: https://careers.dyson.com/en-gb/job-description/digital-optimization-analyst/JR18575?source=Linkedin ?
- A: Yes, I am able to access the job description you linked to on the Dyson careers website. The job title is "Digital Optimization Analyst" and the job description states that the role is responsible for driving digital optimization across Dyson's digital platforms, including websites and mobile apps.

The job duties for this position include analyzing user behavior and data to identify opportunities for improving the user experience and increasing engagement and conversions. The Digital Optimization Analyst will work closely with cross-functional teams to develop and implement optimization strategies, including A/B testing and personalization initiatives. The role also involves monitoring and reporting on the performance of these initiatives, and making data-driven recommendations for further optimization.

The job requirements for this position include a strong background in digital analytics and optimization, with experience using tools such as Google Analytics and Adobe Analytics. The ideal candidate should also have experience with A/B testing, personalization, and website optimization. Strong analytical and problem-solving skills are required, along with the ability to communicate complex data and insights to non-technical stakeholders.

Overall, this position appears to be an excellent opportunity for an experienced digital optimization analyst to work with a leading technology company and help drive improvements to the user experience and business performance of Dyson's digital platforms.
 </p>
 </details>
 
### Q. 영문 공고 받아서 DeepL 또는 Google Translate 사용할 것인가? 한국어 공고를 사용해볼 것인가?


## 7. GPT에 입력할 질문</summary>
### (1) 잡컨설턴트/취업전문가라고 가정
Assume you were a job consultant.

### (2) 링크 또는 텍스트로 된 JD(공고)를 below: 뒤에 붙여넣고 불렛포인트로 된 10개의 면접 질문 리스트, 질문과 답변 리스트 생성
Write 10 the expected interview questions and recommended answer as a list with bullet points,
and gather questions and answers together separately.
Make the questions and answers fit to the Position Job Description below: + JD(채용공고) 복붙 입력받기

<details>
 <summary>*[예시]</summary>
 <p>Write 10 the expected interview questions and recommended answer as a list with bullet points,
and gather questions and answers together separately.
Make the questions and answers fit to the Position Job Description below: (입력) https://careers.dyson.com/en-gb/job-description/digital-optimization-analyst/JR18575?source=Linkedin
 </p>
 </details>
 
### (3) user의 resume(이력서)를 넣고 질문 생성, 예상 질문과 답변 리스트 생성
Write 10 the expected interview questions and recommended answer as a list with bullet points,
and gather questions and answers together separately.
Make the questions and answers fit to this person's experience: + <b>user의 이력서 복붙 입력받기<b>
- (예시) https://www.linkedin.com/in/yoonjikimkr/details/experience/ 내용 copy & paste
 
### (4) user의 resume와 지원하려는 JD(채용공고)에 맞춘 예상 질문과 답변 리스트 생성
Write 10 the expected interview questions and recommended answer as a list with bullet points,
and gather questions and answers together separately.
Make the questions and answers fit to  the Position Job Description(https://careers.dyson.com/en-gb/job-description/digital-optimization-analyst/JR18575?source=Linkedin) and  this person's experience below: + 경험

 

## 8. 개선점
### (1) 효율적인 openAI Chatbot의 사용
- OpenAI API 호출 함수의 효율적인 사용 ➡️ 프로그램 구현시 소모되는 시간 단축
- API 키의 사용의 제한, 지속적 사용시 authentication error 표시되는 경우, 마찬가지로 효율적인 프로그래밍을 통해 조치

### (2) 영문-국문 번역 library 사용하여 해석 제공
- $ pip install googletrans # 무료, 무제한
- $ pip install deepl # key 발급

### (3) Bing Chat API 사용
- 한국어 Q&A, 채용공고 웹주소 사용 가능
- Bing Chat API 이용?
* y - Bing Chat API 사용가능하다면 한국어 Q&A, 채용공고 웹주소 사용 가능.
* n - OpenAI API를 사용하되, 채용공고는 복사 붙여넣기로 입력 받는다.
* SK텔레콤 앱 서비스 마케팅 채널 운영 담당자 채용공고로 테스트 https://thecareers.sktelecom.com/Recruit/Detail/3151 
* Bing Chat 한국어입출력, 웹주소 입력. // 답변 - 성공
 ![BingChat답변](https://user-images.githubusercontent.com/49604099/237019820-800b2bcd-e1fa-4287-875f-1f7758ab46bf.png)
* OpenAI 한국어입출력. 한국어 공고 복붙. // 답변 - 성공
 ![OpenAI답변](https://user-images.githubusercontent.com/49604099/237018571-ea0d0ddf-a184-415d-b411-1995a89b0eff.png)
* OpenAI 한국어입출력. 웹주소. // 답변 - 실패. 관련없는 답변
 ![image](https://user-images.githubusercontent.com/49604099/237020937-9cd0ee48-f310-44b5-b47b-3da2eee51819.png)
* OpenAI 영어질문입력, 한국어출력. 웹주소. // 답변 - 실패. 관련없는 답변
 ![image](https://user-images.githubusercontent.com/49604099/237021834-1422aaf1-0a59-4993-8bfd-e0022b9d98b6.png)


