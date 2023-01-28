import os
import pyautogui as pg
import time

pg.FAILSAFE = False

WORK_FLOW_FOLDER = "D:\\AIBILI\\Project\\my data_2020\\02 workflow\\"
workflow_run_files = ["",
                      "01 html download_전체\\01 html download_1차년도.yxmd",
                      "02 html parsing_게시글\\02 html parsing_게시글.yxmd",
                      ["",
                       "03 html parsing_첨부파일\\03-1 html parsing_01_첨부파일_v0.2.yxmd",
                       "03 html parsing_첨부파일\\03-1 html parsing_02_첨부파일_v0.2.yxmd",
                       "03 html parsing_첨부파일\\03-1 html parsing_03_첨부파일_v0.2.yxmd"],
                       "04 report_전체\\04 report_전체_vO.3.yxmd"]

workflow_take_time = ["",[15],[5],["",15,15,15],[1]] #분단위


def get_file_time(file_path):
    '''
    파일의 마지막 수정 시간,분,초를 반환한다
    '''
    t = time.ctime(os.path.getctime(file_path))
    time_list = t.split()

    y = int(time_list[-1])
    d = int(time_list[2])
    m = time_list[1]
    hour, minue, second = map(int, time_list[3].split(":"))

    return hour, minue, second

def run_yxmd(file_path):
    '''
    ymdx파일을 실행한다
    :param:
        file_path : 경로를 포함한 실행시킬 yxmd파일 명
        i : i번째 실행
        j : (3.첨부파일 다운로드에 대해서) j번째 실행
    :return:
        None
    '''
    print("run",file_path)
    os.startfile(file_path) # 파일열기
    time.sleep(20)
    print("press run")
    pg.hotkey('ctrl', 'r')  # 파일 실행

def run_yxmd_test(file_path):
    print("run",file_path)
    os.startfile(file_path) # 파일열기
    time.sleep(10)
    print("press run")
    pg.hotkey('ctrl', 'r')  # 파일 실행

def check_finish(i,j):
    '''
    현재 실행하는 알트릭스가 끝났는지 확인한다.
    현재는 단순히 시간만 측정하지만,
    추후에 산출되는 파일의 변경시간을 확인하는 식으로 변경(get_file_time함수사용)
    '''
    print(f"time sleep {workflow_take_time[i][j]} minute")
    time.sleep(workflow_take_time[i][j]*60)

if __name__ == '__main__':
    # 파일열기
    for i in range(1,5):
        j=0
        if i==3:
            for _ in range(2):
                for j in range(1,4):
                    file_name = workflow_run_files[i][j]
                    print(f"{i}-{j}")
                    run_yxmd(WORK_FLOW_FOLDER + file_name)
                    check_finish(i, j)
        else:
            file_name = workflow_run_files[i]
            print(f"{i}-{j}")
            run_yxmd(WORK_FLOW_FOLDER+file_name)
            check_finish(i,j)