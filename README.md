# ThrillerAE
 Bien, MJ, Elon
 
## 1. 개인 목표 및 역할
* mj - 웹개발 -> python코드로 작성한 함수를 html문서에서 구현, 
* Bien - 외부 api 연동
* Elon - 데이터 시각화

## 2. 팀명 Thriller Æ
* 스릴러와 같은 감동과 긴장감을 선사하는 프로젝트를 만드는 팀.
* Æ는 인공지능과 사랑을 상징하는 기호로, 라틴 문자 'ash’라고 읽습니다.

## 3. 아이디어 
### (1) 사주/mbti/ - 조건 넣고 gpt 답변 생성해 띄우기
- db 필요없음
- 입력받을 조건 지정
- ChatGPT에 조건, 어조 부여, 답변 생성

### (2) 효율적 일정관리 - 일정 매니저. 답변 내용 저장하여 외부 노트 연동 / 이메일 전송
- db 사용 또는 구글캘린더 등 연동
- ChatGPT에게 일정관리자 역할 부여. Scheduling Atuomation
- Reference: FlowSavvy

### (3) 채용공고 링크/복붙, (선택)LinkedIn 링크/이력 복붙, 예상질문, 모의면접

#### Reference 추천
- 조코딩, 장피엠, 챗지피터스, https://ktestone.com/kapable.github.io/labelSticker/

## 4. 계획<br>
(1) 아이디어 결정 - 5/4까지 (5/3은 reference 찾아보거나 상상 up)<br>
(2) 조건 창에 사용자 입력 받아 답변 생성 Python, ChatGPT api <br>
(3) html, js, css, python <br>
(4) 이미지 생성(MS Designer 등) 또는 첨부 / 디자인 요소 <br>

-------
# Questions List
공고(Job Description)에 관한 것 + 본인에 대한 것

## 앞서
### Q. ChatGPT api가 공고 링크를 읽을 수 있는가?
- 링크드인 링크는 못 불러온다. (As an AI language model, I do not have the ability to access external websites or links. )
-> 공고글을 직접 복붙해와서 읽게 한다.
어라. 링크드인 공고 링크는 못 보는데, 회사 홈 공고 링크는 읽네.

### Q. Linkedin 프로필 링크 읽어들일 수 있는가?
* LinkedIn을 포함하여 소셜 미디어를 보안의 이유로 읽지 못하는 것 같습니다.
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

### 2. 영문 공고 받아서 DeepL 또는 Google Translate 사용할 것인가? 한국어 공고를 사용해볼 것인가?

Regenerate response

## GPT에 입력할 질문
### 1. 잡컨설턴트/취업전문가라고 가정
Assume you were a job consultant.

### 2. 링크 또는 텍스트로 된 JD(공고)를 below: 뒤에 붙여넣고 불렛포인트로 된 10개의 면접 질문 리스트, 질문과 답변 리스트 생성
Write 10 the expected interview questions and recommended answer as a list with bullet points,
and gather questions and answers together separately.
Make the questions and answers fit to the Position Job Description below: + JD(공고) 복붙 입력받기

### ex. Write 10 the expected interview questions and recommended answer as a list with bullet points,
and gather questions and answers together separately.
Make the questions and answers fit to the Position Job Description below: https://careers.dyson.com/en-gb/job-description/digital-optimization-analyst/JR18575?source=Linkedin
- 10 Expected Interview Questions for Digital Optimization Analyst Role:

What do you know about Dyson and our digital platforms?
Recommended Answer: Discuss your research on Dyson and their digital platforms, highlighting any experiences you have had using their products or engaging with their digital channels.

What is your experience with A/B testing and website optimization?
Recommended Answer: Share your experience with A/B testing and website optimization, including specific tools and methodologies you have used in the past.

How would you go about analyzing user behavior and data to identify opportunities for optimization?
Recommended Answer: Discuss your process for analyzing user behavior and data, including any tools or frameworks you have used in the past.

Can you give an example of a successful optimization initiative you led and its impact?
Recommended Answer: Share a specific example of an optimization initiative you led, including the goal, methodology, and impact on business performance.

How would you work with cross-functional teams to implement optimization strategies?
Recommended Answer: Discuss your approach to collaborating with cross-functional teams, including your communication style and methods for ensuring alignment and buy-in.

What is your experience with personalization and targeted marketing?
Recommended Answer: Share your experience with personalization and targeted marketing, including any specific tools or techniques you have used in the past.

What metrics do you use to measure the success of optimization initiatives?
Recommended Answer: Discuss the metrics you typically use to measure the success of optimization initiatives, including how you define and track key performance indicators (KPIs).

How do you stay up-to-date on industry trends and best practices in digital optimization?
Recommended Answer: Share your approach to staying current on industry trends and best practices, including any blogs, publications, or professional organizations you follow or participate in.

Can you walk me through your experience with Google Analytics or other web analytics tools?
Recommended Answer: Provide a brief overview of your experience with Google Analytics or other web analytics tools, highlighting any specific features or reports you are most familiar with.

What do you think are the most important qualities for success in this role?
Recommended Answer: Discuss the qualities you believe are most important for success in this role, such as strong analytical skills, collaboration, communication, and a passion for digital optimization.

Gathered Questions and Answers:

Q: What do you know about Dyson and our digital platforms?
A: Discuss your research on Dyson and their digital platforms, highlighting any experiences you have had using their products or engaging with their digital channels.

Q: What is your experience with A/B testing and website optimization?
A: Share your experience with A/B testing and website optimization, including specific tools and methodologies you have used in the past.

Q: How would you go about analyzing user behavior and data to identify opportunities for optimization?
A: Discuss your process for analyzing user behavior and data, including any tools or frameworks you have used in the past.

Q: Can you give an example of a successful optimization initiative you led and its impact?
A: Share a specific example of an optimization initiative you led, including the goal, methodology, and impact on business performance.

Q: How would you work with cross-functional teams to implement optimization strategies?
A: Discuss your approach to collaborating with cross-functional teams, including your communication style and methods for ensuring alignment and buy-in.

Q: What is your experience with personalization and targeted marketing?
A: Share your experience with personalization and targeted marketing, including any specific tools or techniques you have used in the past.

Q: What metrics do you use to measure the success of optimization initiatives?
A: Discuss the metrics you typically use to measure the success of optimization initiatives, including how you define and track key performance indicators (KPIs).

Q: How do you stay up-to-date on industry trends and best practices in digital optimization?
A: Share your approach to staying current on industry trends and best practices, including any blogs, publications, or professional organizations you follow or participate in.

Q: Can you walk me through your experience with Google Analytics or other web analytics tools?
A: Provide a brief overview of your experience with Google Analytics or other web analytics tools, highlighting any specific features or reports you are most familiar with.

Q: What do you think are the most important qualities for success in this role?
A: Discuss the qualities you believe are most important for success in this role, such as strong analytical skills, collaboration, communication, and a passion for digital optimization.



### 3. user의 resume(이력서)를 넣고 질문 생성, 예상 질문과 답변 리스트 생성
Write 10 the expected interview questions and recommended answer as a list with bullet points,
and gather questions and answers together separately.
Make the questions and answers fit to this person's experience: + user의 이력서 복붙 입력받기

ex. Questions:

Can you tell me about your experience with database queries and building automation?
How have you used data visualization and analysis in your previous roles?
Can you walk me through a project where you analyzed sales data and evaluated sales and marketing effectiveness?
How have you managed shipping samples and handled proposals and expenses in your previous roles?
Have you ever had to modify events or use sales account manager's calls as KPIs in a CRM system before? Can you give me an example?
Can you tell me about a time when you had to manage a large amount of data and ensure its accuracy?
How have you used Excel spreadsheets and CRM systems in your previous roles?
Can you tell me about a time when you had to improve communication with colleagues or other companies and how you achieved it?
Have you ever worked with QuickBooks or other accounting software? Can you tell me about your experience?
Can you walk me through a project where you had to translate information from one language to another?
Answers:

Yes, I have experience in both database queries and building automation. In my previous role as a Database Operator at IQVIA, I frequently wrote SQL queries to extract and manipulate data from various databases. I also used Python to automate repetitive tasks such as generating daily reports and updating databases.
In my previous roles, I used data visualization and analysis to evaluate the effectiveness of sales and marketing campaigns. For example, while working as an Operations Specialist at Galderma, I created quarterly SIC trend charts to identify market trends and to help the sales and marketing teams plan their strategies. I also generated ad-hoc sales reports with clinics' sell-out data and evaluated quarterly incentives with KPIs to help interpret how the sales team was tracking against goals.
When I worked as a Data Analyst on a contract basis, I managed the sales database, analyzed sales data by account manager, account, and segment, and evaluated aesthetics and prescription medicine sales incentive from internal data, including sales out and total revenue, to provide a better understanding of sales and marketing effectiveness. I worked closely with the sales and marketing teams to provide insights and recommendations on how to improve their performance.
Yes, I have experience managing shipping samples and handling proposals and expenses in my previous roles. For example, while working at Galderma, I managed the shipping of medical devices and prescriptions and handled proposals and expenses of bureaus. I also entered or changed supplier and adjusted prices and discount rates on ERP (iScala).
Yes, I have modified events and used each sales account manager's call and hands-on seminar as one of KPIs on Veeva (Salesforce) in my previous roles. For example, while working at Galderma, I modified events and used the sales account manager's calls and hands-on seminars as a KPI to measure their performance and to identify areas for improvement.
Yes, I have experience managing a large amount of data and ensuring its accuracy. For example, while working as an Accounting Intern at EGBI, I managed the receipts for EGBI's bookkeeping clients using Hubdoc and entered transactions into QuickBooks. I ensured the accuracy of the data by reconciling the accounts and double-checking the entries.
I have used Excel spreadsheets extensively in my previous roles, especially for data analysis and reporting. I am proficient in creating pivot tables and charts and using advanced functions such as VLOOKUP and IF statements. I have also used CRM systems such as Salesforce and Veeva to manage customer relationships and sales data.
One time when I had to improve communication with colleagues and other companies was while working as a Marketing Intern at U-MEDI. I improved my communication


### 4. user의 resume와 지원하려는 JD에 맞춘 예상 질문과 답변 리스트 생성
Write 10 the expected interview questions and recommended answer as a list with bullet points,
and gather questions and answers together separately.
Make the questions and answers fit to this person's experience and the Position Job Description:


### Rezi.ai (Resumebuiler)
<Experience>
1. What was your **role** at the company? ex. Marketing Analyst
2. For which **company** did you work? ex. Google
3. How Long were you with the company? ex. May 2023 - May 2023
4. WHere was the company located? ex. New York
5. What did you do at the company? ex. Organized and implemented Google Analytics data tracking campaigns to maximize the effectiveness of email remarketing initiatives that were deployed using Salesforce's marketing cloud software.

<Project>
1. Give your project a **title**. ex. Volunteer
2. In which **organization** did you do your project? ex.Habitat for Humanity
3. **When** did you do your project? ex. May 2023 - May 2023
4. Now describe what **you did**. ex. Voluteered to help renovate a house and managed a team of 6.

<Education>
1. **Degree** **Qualification** **major**
<Certifications>
<Coursework>
<Involvement>
<Skills>
<Summary>

