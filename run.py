from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import schedule
from webdriver_manager.chrome import ChromeDriverManager


def input_forms():
    options = Options()
    options.add_argument("--headless")
    # browser = webdriver.Chrome("chromedriver.exe", options=options)

    # chromedriverを使ってブラウザを起動（exeを指定するのはwindows専用）
    # browser = webdriver.Chrome("chromedriver.exe")

    # webdriver_managerを使ってブラウザを起動
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # 指定のURLにアクセスする
    url = "https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAa__ZUHFKtUNERIMTRYVUJUQjhXU0ZDNE5CS0ZOUTUzUi4u"
    browser.get(url)


    # フォームに入力する

    # class名で指定する（classは複数ある場合はリスト形式で読み込む）
    elem_name = browser.find_elements_by_class_name("office-form-question-textbox")
    elem_name[1].send_keys("uji")
    elem_name[2].send_keys("Herokuから入力")

    # ラジオボタンをクリックする（value属性で指定する方法）
    elem_radio = browser.find_element_by_xpath("//input[@value='冬']")
    elem_radio.click()

    # 送信ボタンをクリックする
    elem_button = browser.find_element_by_class_name("office-form-bottom-button")
    elem_button.click()


    sleep(5)

    # ブラウザを終了する
    browser.quit()

    print("execute run.")

def main():
    schedule.every(30).seconds.do(input_forms)

    while True:
        schedule.run_pending()
        sleep(1)

if __name__ == "__main__":
    main()