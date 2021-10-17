###文件描述
####Config.py
>**config**中填写需要导入的学生学号信息,登录密码, 
**username**与**password**可以只用一个人的,只需修改schedule_link中的以及日期term_time和stu_id

####Schedule.py
>Schedule主要用于获取当前学生的课表信息,并且并返回一个包含所有学生的课表
####DealDate.py
>将Schedule中的返回的课程列表传入DataFrame中,然后在将数据处理成以下格式:
 ```text
{
  "student": "某人",
  "xuehao": "XXX",
  "password": "XXXXXXXXXXX",
  "course": [
    {
      "name": "1",
      "teacher": "a",
      "room": "100",
      "ddd": "XXXXXXXX",
      "days": 3,
      "nums" : "1",
      "enums" : "2",
      "attend": "10,12,1,12.."
    },
    {
      "name": "2",
      "teacher": "b",
      "room": "100",
      "ddd": "周几第几节{几到几周}", //描述性文字
      "days": 4,  //周几
      "nums" : "1", //开始的时间
      "enums" : "2", //截止时间
      "attend": "10,12,1,12,12" //上课的周
    }
  ]
}
```
####main.py
>主程序运行



