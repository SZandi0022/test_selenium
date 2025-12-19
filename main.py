
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# تنظیمات chrom
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=Options()
)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("detach", True)
driver.maximize_window()
driver.get("https://demoqa.com")



#پر کردن فیلدهای فرم
driver.get("https://demoqa.com/text-box")

search_fild= driver.find_element("id", "userName")
search_fild.send_keys("saeid zandi")
search_fild.clear()     #پاک کردن فیلد
search_fild.send_keys("saeid zandi")
time.sleep(2) #وقفه

search_fild1 = driver.find_element("id", "userEmail")
search_fild1.send_keys("example@gmail.com")
search_fild1 .clear()
time.sleep(2)
search_fild1.send_keys("example@gmail.com")

search_fild2 = driver.find_element("id", "currentAddress")
search_fild2.send_keys("Iran-Tehran: niyavaran")


search_fild3=driver.find_element("id", "permanentAddress")
search_fild3.send_keys("Iran - Iran")
time.sleep(2)
search_fild3.send_keys(Keys.CONTROL + "a")  # انتخاب همه حذف کاراکتر
search_fild3.send_keys(Keys.BACKSPACE)
search_fild3.send_keys("Iran - Iran")
#ارسال فرم
button_search=driver.find_element("id", "submit")
button_search.click()


#اعتبار سنجی

# 2. اعتبارسنجی نتیجه
try:
    # صبر کن تا بخش نتیجه ظاهر شود
    result_section = wait.until(
        EC.presence_of_element_located((By.ID, "output"))
    )

    # بررسی نمایش اطلاعات
    name_result = driver.find_element(By.ID, "name").text
    email_result = driver.find_element(By.ID, "email").text

    # چک کن که داده‌ها صحیح نمایش داده شده‌اند
    assert "علی رضایی" in name_result, f"نام نمایش داده شده صحیح نیست: {name_result}"
    assert "test@example.com" in email_result, f"ایمیل نمایش داده شده صحیح نیست: {email_result}"

    print("✅ تست موفقیت‌آمیز بود! فرم صحیح ارسال شد.")
    print(f"نام نمایش داده شده: {name_result}")
    print(f"ایمیل نمایش داده شده: {email_result}")

except Exception as e:
    print(f"❌ تست با خطا مواجه شد: {e}")
    # عکس از صفحه در لحظه خطا بگیرید
    driver.save_screenshot("error_screenshot.png")

finally:
    time.sleep(10)  # برای مشاهده نتیجه
   # driver.quit()




