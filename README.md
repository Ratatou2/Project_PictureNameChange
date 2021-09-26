# [📚 Project] Picture_Name_Change 
---
무작위 순서의 이미지들에 **순차적인 번호를 부여**하는 프로그램
This program **gives sequential names** to randomly named files


## 특징(Features)
---
이 프로그램은 아래와 같은 경우에도 사용 가능합니다
- 무작위명 파일들을 순차적으로 변경하고 싶을 때
-  확장자 A에서 확장자 B로 변경할 때(ex. jpg → .png)
- 확장자 별로 변경하고 싶을 경우(ex. jpg만 이름 변경)
- 도저히 손으로 하나하나 파일명을 변경할 수 없을 때

![image](https://user-images.githubusercontent.com/61686603/134800902-558b34ac-dc02-49b2-b72c-ca4661b54518.png)


## 사용법(How to use)
----
[![BLOG](https://user-images.githubusercontent.com/61686603/134764944-efad448d-6403-4782-a996-b217670a5657.png)](https://blog.naver.com/ws4232/222039746417)


**First** : 제일 먼저 파일을 실행시키고, 사진이 저장되어있는 파일 경로를 입력해주면 된다
``` python
출처 : https://blog.naver.com/ws4232
[Please enter a path]
D:\python
```
- 나같은 경우엔 D:\python에 테스트용 사진을 모아두었음
- 파일 경로 확인 하는 방법은 맨 아래에 첨부

**Second** : 그 다음은 이제 내가 원하는 확장자를 가진 파일을 입력하면 된다
``` python
[Enter the extension you are looking for]
ex) .jpg , .pdf , .png , .avi , .mp4
※ <<If you don't enter anything, all files in that path will be selected>>
```
- .jpg 확장자를 가진 파일만 선택하고 싶다면 .jpg 입력하고 엔터치면 됨
- 사진처럼 공백으로 두고 엔터치면 해당 경로에 있는 모든 파일이 선택됨

**Third** : 내가 변경하고자 하는 확장자를 입력해주면 된다, 나는 png로 변경할 예정
``` python
[What do you want to change the extension to?]
ex) .jpg , .pdf , .png , .avi , .mp4
.png
```

**Fourth** : 처음 시작할 숫자를 입력하면 되는데 대개는 1을 입력한다
``` python
[Enter a number to be the name of the file]
1
```
- 여기서 **주의사항**이 있는데 해당 경로에 이름이 겹치는 파일이 있다면, 이 코드는 동작하지 않는다
- 예를들어 내가 1~100 으로 설정하길 바라는데, 해당 경로에 이미 1~100 사이의 숫자를 가진 파일이 하나라도 있다면 에러가 난다
- 이럴땐 임의의 숫자를 입력하면된다
- 예를들어 123456를 입력하면 첫 파일 이름이 123456으로 설정되고 그 이후로 1씩 커지면서 저장된다
- 그러고난 후에 다시 이 코드를 똑같이 동작시켜서 1을 입력하면 해결된다
- 한줄 요약 : 에러나면 엄청 큰 임의의 숫자 하나 입력하고, 다시 돌리면 9할은 해결된다
- 이름이 같은 파일을 처리하는 코드가 없어서 생기는 에러 ㅠ

