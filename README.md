# job_task_questions
для локального запуска проекта просто пропишите docker compose up --build  

пример запроса:  
curl -X 'POST' \  
  'http://127.0.0.1:8080/questions' \  
  -H 'accept: application/json' \  
  -H 'Content-Type: application/json' \  
  -d '{  
  "questions_num": 1  
}'  

faq: на линуксе все должно подняться с первого раза, но на винде возможно придется сначала подождать пока докер создаст вольюм постгреса и поднять еще раз
