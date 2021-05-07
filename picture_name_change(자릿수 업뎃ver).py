#[파일 이름 일괄 변경(숫자로 변경)]

# os 명령어 쓸거라서 import 해줘야 함
import os

# 이거는 사진이 존재하는 경로를 입력해주면 된다 (아래와 같은 형식으로)
# ex) D:\python\picture
print("출처 : https://blog.naver.com/ws4232")
print("[Please enter a path]")
file_path = input()

# 검색할 확장자를 입력해주면 된다.

print("\n[Enter the extension you are looking for]")
print("ex) .jpg , .pdf , .png , .avi , .mp4")
print("※ <<If you don't enter anything, all files in that path will be selected>>")
extension = input()
#if extension == 0:
    
# 변경하고자 하는 확장자를 입력해주면 된다

print("\n[What do you want to change the extension to?]")
print("ex) .jpg , .pdf , .png , .avi , .mp4")
chage_ext = input()

# 아까 입력해준 디렉토리에 있는 것들을 전부 찾아오는 것
file_list = os.listdir(file_path)

# 아까 입력해준 확장자에 해당하는 파일을 file_list_py에 전부 집어 넣는다
file_list_py = [file for file in file_list if file.endswith(extension)] 


print("\n[Enter a number to be the name of the file]")
i = int(input())
#시작할 파일명 

print("\n[How many zeros do you want to fill in the front?]")
print("ex) 2 = 01 / 3 = 001 / 4 = 0001 / 5 = 00001로 시작함")
z = int(input())
# 예를들어 001 ~ 로 시작하기 위한 자릿수를 정하는 것임


# 대충 설명하자면 file_list_py에 들어있는 것들을 하나씩 가져오는 반복문
# 일단 가져오면 dst에 넣어서 숫자 + 내가 원하는 확장자로 변경해주는 것임
# 그렇게 os.rename으로 해당 파일은 dst에 적힌대로 고대로 저장~

for name in file_list_py:
    src = os.path.join(file_path, name)
    dst = str(i).zfill(z) + chage_ext
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1

# 없어도 되긴하는데 끝난지 알고 싶어서 넣었음

print("End")